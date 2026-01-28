class PanelPCClient:
    def __init__(self, host, port):
        self.url = f"http://{host}:{port}"
    
    def send_selected_crop(self, crop: str) -> None:
        # In real code this would be a HTTP(S) call to the backend API
        print(f"[IPC] selected_crop={crop}")
