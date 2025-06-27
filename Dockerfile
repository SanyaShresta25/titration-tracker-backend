FROM conda/miniconda3

WORKDIR /app
COPY environment.yml ./
RUN conda env create -f environment.yml

COPY . .

SHELL ["conda", "run", "-n", "smiles3d", "/bin/bash", "-c"]

RUN pip install flask flask-cors

CMD ["conda", "run", "-n", "smiles3d", "python", "app.py"]
