# File Converter API

A simple FastAPI backend to **upload `.rar` files, convert them to `.zip`**, and download the converted files.  

## Features

- **Health check** endpoint (`GET /api/`) → returns `{"status": "ok"}`
- **Upload `.rar` files** (`POST /api/upload`)
- **Convert uploaded `.rar` to `.zip`** (`POST /api/convert?filename=<filename>`)
- **Download converted files** (`GET /api/download/{filename}`)
- Automatic **temporary filenames** and cleanup of `.rar` files after conversion
- FastAPI **Swagger UI** documentation available at `/docs`

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/` | GET | Health check |
| `/api/upload` | POST | Upload a `.rar` file |
| `/api/convert` | POST | Convert uploaded `.rar` to `.zip` (requires `filename` query param) |
| `/api/download/{filename}` | GET | Download a converted `.zip` file |

## Example Usage

### Health check
```bash
curl http://localhost:8000/api/
```

### Upload a file

```bash
curl -F "file=@example.rar" http://localhost:8000/api/upload
```

### Convert file

```bash
curl -X POST "http://localhost:8000/api/convert?filename=<your_uploaded_filename>"
```

### Download file

```bash
curl -O http://localhost:8000/api/download/<converted_filename>.zip
```

## Installation (for local development)

1. Clone the repository:

```bash
git clone https://github.com/yourusername/file-converter-api.git
cd file-converter-api
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the API locally:

```bash
uvicorn app.main:app --reload
```

Open [http://localhost:8000/docs](http://localhost:8000/docs) to see Swagger UI.

## Docker

Build and run the Docker container:

```bash
docker build -t file-converter-api .
docker run -p 8000:8000 file-converter-api
```

* Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

## Notes

* The backend **does not use a database**; all uploaded files are handled in the `uploads/` folder.
* The `uploads/` folder is temporary; files are deleted after conversion.
* FastAPI automatically provides **Swagger UI** (`/docs`) and **OpenAPI JSON** (`/openapi.json`).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
