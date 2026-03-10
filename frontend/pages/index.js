import { useState } from "react";
import UploadBox from "../components/UploadBox";
import ResultPanel from "../components/ResultPanel";

export default function Home() {
  const [file, setFile] = useState(null);
  const [res, setRes] = useState(null);

  async function analyze() {
    const form = new FormData();
    form.append("file", file);

    const r = await fetch("http://localhost:8000/analyze", {
      method: "POST",
      body: form,
    });

    setRes(await r.json());
  }

  async function generatePDF() {
    const r = await fetch("http://localhost:8000/pdf", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(res),
    });

    const data = await r.json();

    const link = document.createElement("a");
    link.href = "data:application/pdf;base64," + data.pdf;
    link.download = "TaurgoVision_Report.pdf";
    link.click();
  }

  return (
    <div>
      <div className="card">
        <h1 style={{ marginBottom: 20, color: "#111" }}>TaurgoVision</h1>

        <UploadBox onSelect={setFile} />

        <button onClick={analyze} disabled={!file}>
          Analyze
        </button>

        {res && (
          <>
            <ResultPanel result={res} />

            <button
              onClick={generatePDF}
              style={{ marginTop: 20, background: "#28a745" }}
            >
              Download PDF Report
            </button>
          </>
        )}
      </div>
    </div>
  );
}