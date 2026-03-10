export default function ResultPanel({ result }) {
  if (!result) return null;

  return (
    <div style={{ marginTop: 40 }}>
      {/* --- IMAGES --- */}
      <h2 style={{ color: "#111" }}>Inspection Results</h2>

      <div className="image-row">
        <div className="image-box">
          <h3 style={{ color: "#111" }}>Original</h3>
          <img
            src={`data:image/jpeg;base64,${result.original_image}`}
            alt="original"
          />
        </div>

        <div className="image-box">
          <h3 style={{ color: "#111" }}>Overlay</h3>
          <img
            src={`data:image/jpeg;base64,${result.overlay_image}`}
            alt="overlay"
          />
        </div>
      </div>

      {/* --- SUMMARY --- */}
      <div className="section-box">
        <h3 style={{ color: "#111" }}>Summary</h3>
        <p style={{ color: "#333", marginTop: 10 }}>
          {result.summary}
        </p>
      </div>

      {/* --- DEFECTS --- */}
      <div className="section-box">
        <h3 style={{ color: "#111" }}>Detected Defects</h3>

        <div style={{ marginTop: 15 }}>
          {result.defects.length === 0 && (
            <p style={{ color: "#333" }}>No defects detected.</p>
          )}

          {result.defects.length > 0 && (
            <table style={{ width: "100%", borderCollapse: "collapse" }}>
              <thead>
                <tr>
                  <th style={thStyle}>Type</th>
                  <th style={thStyle}>Severity</th>
                  <th style={thStyle}>Confidence</th>
                  <th style={thStyle}>Notes</th>
                </tr>
              </thead>
              <tbody>
                {result.defects.map((d, i) => (
                  <tr key={i}>
                    <td style={tdStyle}>{d.type}</td>

                    <td style={tdStyle}>
                      <span style={{
                        padding: "4px 10px",
                        borderRadius: "6px",
                        fontWeight: "bold",
                        color: "#fff",
                        background:
                          d.severity === "High"
                            ? "#d9534f"
                            : d.severity === "Moderate"
                            ? "#f0ad4e"
                            : "#5cb85c",
                      }}>
                        {d.severity}
                      </span>
                    </td>

                    <td style={tdStyle}>{(d.confidence * 100).toFixed(1)}%</td>
                    <td style={tdStyle}>{d.notes}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </div>
      </div>

      {/* --- RECOMMENDATIONS --- */}
      <div className="section-box">
        <h3 style={{ color: "#111" }}>Recommendations</h3>
        <ul style={{ marginTop: 10, color: "#333", lineHeight: "1.8" }}>
          {result.recommendations.map((r, idx) => (
            <li key={idx}>{r}</li>
          ))}
        </ul>
      </div>
    </div>
  );
};

const thStyle = {
  padding: "10px",
  textAlign: "left",
  borderBottom: "2px solid #ccc",
  color: "#111",
};

const tdStyle = {
  padding: "10px",
  color: "#333",
  borderBottom: "1px solid #ddd",
  verticalAlign: "top",
};