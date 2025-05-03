import http.server
import socketserver

def run_simple_http_server(directory: str = '.', port: int = 8000) -> None:
    """Runs a simple HTTP server serving files from the specified directory."""
    os.chdir(directory)
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), Handler) as httpd:
        print(f"Serving HTTP on port {port} from directory {directory}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

# Example usage:
# if __name__ == "__main__":
#     run_simple_http_server(directory='.', port=8080)