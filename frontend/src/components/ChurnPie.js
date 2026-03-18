import { PieChart, Pie, Cell } from "recharts";

export default function ChurnPie({ data }) {
  const counts = { High: 0, Medium: 0, Low: 0 };

  data.forEach(d => counts[d.risk]++);

  const chartData = Object.keys(counts).map(k => ({
    name: k,
    value: counts[k]
  }));

  return (
    <div className="card">
      <h3>Churn Distribution</h3>
      <PieChart width={300} height={300}>
        <Pie data={chartData} dataKey="value">
          {chartData.map((_, i) => <Cell key={i} />)}
        </Pie>
      </PieChart>
    </div>
  );
}