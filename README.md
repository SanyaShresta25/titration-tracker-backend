## 🧪 RDKit Flask Backend – SMILES to SDF Generator

This backend service accepts a SMILES string and returns a 3D-optimized SDF file using RDKit.

---

### 📂 Folder: `titration-tracker-backend/`

### 🚀 Run with Python (No Docker)

#### Prerequisites:

* Python 3.10+
* [RDKit](https://www.rdkit.org/docs/Install.html) (install via Conda recommended)

```bash
# Create Conda environment
conda create -n rdkitenv python=3.10 -y
conda activate rdkitenv

# Install packages
conda install -c rdkit rdkit -y
pip install flask flask-cors

# Run the app
python app.py
```

The app will run at: [http://localhost:5000](http://localhost:5000)

---

### 📄 Sample Request

```bash
curl -X POST http://localhost:5000/sdf \
  -H "Content-Type: application/json" \
  -d '{"smiles": "CCO"}'
```

You will receive an SDF string as response.

---

### 🛠️ Run with Docker

#### Dockerfile:

```dockerfile
FROM continuumio/miniconda3

WORKDIR /app
COPY app.py .

RUN conda create -n rdkitenv python=3.10 -y && \
    echo "conda activate rdkitenv" >> ~/.bashrc && \
    /bin/bash -c "source ~/.bashrc && conda activate rdkitenv && pip install flask flask-cors && conda install -c rdkit rdkit -y"

CMD ["/bin/bash", "-c", "source ~/.bashrc && conda activate rdkitenv && python app.py"]
```

#### Build and Run:

```bash
cd titration-tracker-backend
docker build -t titration-backend .
docker run -d -p 5000:5000 titration-backend
```

---

### 📊 Endpoint

* `POST /sdf`

  * Input: JSON with `smiles` key
  * Output: `chemical/x-mdl-sdfile` SDF string

---

### 📚 Example Frontend Call

```ts
fetch("http://localhost:5000/sdf", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ smiles: "CCO" })
})
  .then(res => res.text())
  .then(sdf => console.log("SDF Output:", sdf));
```

---

### 📖 Technologies Used

* Flask (Python)
* RDKit
* Flask-CORS
* Docker

---

### 👨‍💻 Author

**Sanya Shresta**
GitHub: [@SanyaShresta25](https://github.com/SanyaShresta25)
