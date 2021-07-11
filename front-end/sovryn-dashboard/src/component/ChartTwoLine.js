import React from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend
} from "recharts";


export default function ChartTwoLine({data}) {
  return (
    <LineChart
      width={950}
      height={220}
      data={data}
      margin={{
        top: 5,
        right: 30,
        left: 20,
        bottom: 5
      }}
    >
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="date" />
      <YAxis />
      <Tooltip />
      <Legend />
      <Line
        type="monotone"
        dataKey="Mint"
        stroke="teal"
        
      />
      <Line
        type="monotone"
        dataKey="Burn"
        stroke="red"
        
      />
    </LineChart>
  );
}
