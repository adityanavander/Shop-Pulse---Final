export default function Filters({ segment, setSegment, risk, setRisk, search, setSearch }) {
  return (
    <div style={{ marginTop: "20px" }}>
      <input
        placeholder="Search Customer"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />

      <select onChange={(e) => setSegment(e.target.value)}>
        <option value="">All Segments</option>
        <option value="High">High</option>
        <option value="Medium">Medium</option>
        <option value="Low">Low</option>
      </select>

      <select onChange={(e) => setRisk(e.target.value)}>
        <option value="">All Risk</option>
        <option value="High">High</option>
        <option value="Medium">Medium</option>
        <option value="Low">Low</option>
      </select>
    </div>
  );
}