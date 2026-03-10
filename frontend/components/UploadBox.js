import { useState } from "react";

export default function UploadBox({ onSelect }) {
  const [name, setName] = useState("");

  function handleFile(e) {
    const file = e.target.files[0];
    if (!file) return;

    setName(file.name);
    onSelect(file);
  }

  return (
    <div style={{ marginBottom: "15px" }}>
      <label style={{ fontWeight: "bold", color: "#000" }}>Choose File</label>
      <br />
      <input
        type="file"
        accept=".jpg,.jpeg,.png,.heic,.HEIC"
        onChange={handleFile}
        style={{
          marginTop: "8px",
          marginBottom: "8px",
          color: "#000",
          fontWeight: "600"
        }}
      />

      {name && (
        <p style={{ marginTop: "5px" }}>
          <span style={{ color: "#000", fontWeight: "bold" }}>Selected: </span>
          <span style={{ color: "#000", fontWeight: "600" }}>{name}</span>
        </p>
      )}
    </div>
  );
}