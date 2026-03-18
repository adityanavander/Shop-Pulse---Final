import { BarChart, Bar, XAxis, YAxis } from "recharts";

export default function RevenueBar({ data }) {
  const seg = {};

  data.forEach(d => {
    seg[d.segment] = (seg[d.segment] || 0) + Number(d.monetary || 0);
  });

  const chartData = Object.keys(seg).map(k => ({
    name: k,
    value: seg[k]
  }));

  return (
    <div className="card">
      <h3>Revenue by Segment</h3>
      <BarChart width={400} height={300} data={chartData}>
        <XAxis dataKey="name" />
        <YAxis />
        <Bar dataKey="value" />
      </BarChart>
    </div>
  );
}