from flask import Flask, request, jsonify
import pandas as pd
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    file_path = data['filePath']
    file_type = data['fileType']

    if file_type == 'csv':
        df = pd.read_csv(file_path)
    elif file_type == 'xlsx':
        df = pd.read_excel(file_path)
    else:
        return jsonify({"error": "Unsupported file type"}), 400

    column_types = {col: 'numeric' if pd.api.types.is_numeric_dtype(df[col]) else 'categorical' for col in df.columns}

    suggested_charts = [
        {"column": col, "chartType": "Line, Histogram, Scatter" if colType == 'numeric' else "Bar, Pie"}
        for col, colType in column_types.items()
    ]

    return jsonify({"columns": list(df.columns), "suggestedCharts": suggested_charts})

if __name__ == '__main__':
    app.run(port=5001, debug=True)
