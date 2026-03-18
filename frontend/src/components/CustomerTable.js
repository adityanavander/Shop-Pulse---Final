export default function CustomerTable({ data }) {
  return (
    <table style={{ width: "100%", marginTop: "20px", borderCollapse: "collapse" }}>
      <thead>
        <tr>
          <th>ID</th>
          <th>Segment</th>
          <th>Revenue</th>
          <th>Risk</th>
        </tr>
      </thead>

      <tbody>
        {data.slice(0, 10).map((d, i) => (
          <tr key={i}>
            <td>{d.customer_id}</td>
            <td>{d.segment}</td>
            <td>₹{d.monetary}</td>
            <td>{d.risk}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}