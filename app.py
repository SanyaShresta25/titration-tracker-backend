from flask import Flask, request, Response
from rdkit import Chem
from rdkit.Chem import AllChem
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/sdf", methods=["POST"])
def generate_sdf():
    data = request.get_json()
    smiles = data.get("smiles", "")

    mol = Chem.MolFromSmiles(smiles)
    if not mol:
        return Response("Invalid SMILES", status=400)

    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol, AllChem.ETKDG())
    AllChem.UFFOptimizeMolecule(mol)

    sdf = Chem.MolToMolBlock(mol)
    return Response(sdf, mimetype="chemical/x-mdl-sdfile")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
