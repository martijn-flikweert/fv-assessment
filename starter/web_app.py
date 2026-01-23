from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import Any

import ui
from state import GLOBAL_D

BASE_DIR = Path(__file__).parent


def load_json(name: str) -> dict[str, Any]:
    return json.loads((BASE_DIR / name).read_text())


HTML = """<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Panel PC Assessment</title>
    <style>
      body { font-family: Arial, sans-serif; margin: 20px; }
      h1 { margin-bottom: 8px; }
      .row { display: flex; gap: 24px; }
      .panel { border: 1px solid #ddd; padding: 12px; border-radius: 6px; min-width: 280px; }
      select { width: 100%; padding: 6px; }
      .defect { padding: 4px 0; }
      .badge { display: inline-block; padding: 2px 6px; border-radius: 4px; font-size: 12px; margin-left: 8px; }
      .visible { background: #e6f6e6; color: #1b5e20; }
      .ignore { background: #fff8e1; color: #8d6e63; }
      .hidden { background: #ffebee; color: #b71c1c; }
      .meta { color: #666; font-size: 12px; }
    </style>
  </head>
  <body>
    <h1>Panel PC Assessment</h1>
    <div class="meta" id="meta"></div>
    <div class="row">
      <div class="panel">
        <h3>Crops</h3>
        <select id="cropSelect"></select>
        <button id="selectBtn">Select</button>
        <div class="meta" id="selectedCrop"></div>
      </div>
      <div class="panel">
        <h3>Visible Defects</h3>
        <div id="defects"></div>
      </div>
    </div>
    <script>
      async function getJson(path) {
        const res = await fetch(path);
        return res.json();
      }

      function renderDefects(defects) {
        const container = document.getElementById("defects");
        container.innerHTML = "";
        for (const item of defects) {
          if (typeof item === "string") {
            const div = document.createElement("div");
            div.className = "defect";
            div.textContent = item;
            container.appendChild(div);
          } else {
            const div = document.createElement("div");
            div.className = "defect";
            div.textContent = item.label || item.key;
            if (item.status) {
              const badge = document.createElement("span");
              badge.className = "badge " + item.status;
              badge.textContent = item.status;
              div.appendChild(badge);
            }
            container.appendChild(div);
          }
        }
      }

      async function load() {
        const state = await getJson("/api/state");
        const crops = await getJson("/api/crops");
        const defects = await getJson("/api/defects");

        document.getElementById("meta").textContent =
          `Machine: ${state.machine_id || "?"} | Customer: ${state.customer || "?"}`;

        const select = document.getElementById("cropSelect");
        select.innerHTML = "";
        for (const c of crops) {
          const opt = document.createElement("option");
          opt.value = c;
          opt.textContent = c;
          select.appendChild(opt);
        }

        renderDefects(defects);
        document.getElementById("selectedCrop").textContent = `Selected: ${state.selected_crop || "-"}`;
      }

      document.getElementById("selectBtn").addEventListener("click", async () => {
        const crop = document.getElementById("cropSelect").value;
        await fetch("/api/select_crop", {
          method: "POST",
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify({crop})
        });
        const state = await getJson("/api/state");
        document.getElementById("selectedCrop").textContent = `Selected: ${state.selected_crop || "-"}`;
      });

      load();
    </script>
  </body>
</html>
"""


class Handler(BaseHTTPRequestHandler):
    def _send_json(self, payload: Any, status: int = 200) -> None:
        data = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _send_html(self, html: str, status: int = 200) -> None:
        data = html.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self) -> None:
        if self.path == "/":
            self._send_html(HTML)
            return

        if self.path == "/api/state":
            config = load_json("config.json")
            state = {
                "machine_id": config.get("machine", {}).get("id"),
                "customer": GLOBAL_D.get("customer"),
                "selected_crop": GLOBAL_D.get("selected_crop"),
            }
            self._send_json(state)
            return

        if self.path == "/api/crops":
            config = load_json("config.json")
            crops = ui.get_available_crops(config)
            self._send_json(crops)
            return

        if self.path == "/api/defects":
            # render_defect_sliders may return list[str] or list[dict]
            defects = ui.render_defect_sliders()
            self._send_json(defects)
            return

        self._send_json({"error": "not found"}, status=404)

    def do_POST(self) -> None:
        if self.path == "/api/select_crop":
            length = int(self.headers.get("Content-Length", "0"))
            raw = self.rfile.read(length) if length else b"{}"
            payload = json.loads(raw.decode("utf-8"))
            crop = payload.get("crop")
            if not crop:
                self._send_json({"error": "crop missing"}, status=400)
                return
            ui.select_crop(crop)
            self._send_json({"ok": True, "selected_crop": crop})
            return

        self._send_json({"error": "not found"}, status=404)


def run(host: str = "127.0.0.1", port: int = 8000) -> None:
    server = HTTPServer((host, port), Handler)
    print(f"Serving assessment UI at http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run()
