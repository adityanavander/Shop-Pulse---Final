import React, { useEffect, useState } from "react";
import "./App.css";

import Sidebar from "./components/Sidebar";
import KPIcards from "./components/KPIcards";
import Filters from "./components/Filters";
import ChurnPie from "./components/ChurnPie";
import RevenueBar from "./components/RevenueBar";
import CustomerTable from "./components/CustomerTable";

import { loadCustomerData } from "./utils/loadData";

function App() {
  const [data, setData] = useState([]);
  const [segment, setSegment] = useState("");
  const [risk, setRisk] = useState("");
  const [search, setSearch] = useState("");

  useEffect(() => {
    loadCustomerData(setData);
  }, []);

  const filtered = data.filter(
    (d) =>
      (segment ? d.segment === segment : true) &&
      (risk ? d.risk === risk : true) &&
      (search ? d.customer_id?.includes(search) : true)
  );

  return (
    <div className="app">
      <Sidebar />

      <div className="main">
        <h1>ShopPulse Dashboard</h1>

        <KPIcards data={filtered} />

        <Filters
          segment={segment}
          setSegment={setSegment}
          risk={risk}
          setRisk={setRisk}
          search={search}
          setSearch={setSearch}
        />

        <div className="charts">
          <ChurnPie data={filtered} />
          <RevenueBar data={filtered} />
        </div>

        <CustomerTable data={filtered} />
      </div>
    </div>
  );
}

export default App;