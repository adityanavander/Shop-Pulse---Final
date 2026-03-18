export default function KPIcards({ data }) {
  const revenue = data.reduce((s, d) => s + Number(d.monetary || 0), 0);

  return (
    <div style={{ display: "flex", gap: "20px" }}>
      <div className="card">Revenue: ₹{revenue}</div>
      <div className="card">Customers: {data.length}</div>
    </div>
  );
}