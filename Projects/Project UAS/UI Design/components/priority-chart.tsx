"use client"

import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from "recharts"

interface Task {
  id: number
  name: string
  priority: number
}

interface PriorityChartProps {
  tasks: Task[]
}

export default function PriorityChart({ tasks }: PriorityChartProps) {
  const chartData = [...tasks]
    .sort((a, b) => b.priority - a.priority)
    .slice(0, 5)
    .map((task) => ({
      name: task.name.length > 20 ? task.name.substring(0, 20) + "..." : task.name,
      priority: Math.round(task.priority),
      fullName: task.name,
    }))

  return (
    <ResponsiveContainer width="100%" height={300}>
      <BarChart data={chartData} margin={{ top: 20, right: 30, left: 0, bottom: 60 }}>
        <CartesianGrid strokeDasharray="3 3" stroke="hsl(var(--color-border))" />
        <XAxis
          dataKey="name"
          angle={-45}
          textAnchor="end"
          height={100}
          tick={{ fontSize: 12, fill: "hsl(var(--color-muted-foreground))" }}
        />
        <YAxis tick={{ fontSize: 12, fill: "hsl(var(--color-muted-foreground))" }} domain={[0, 100]} />
        <Tooltip
          contentStyle={{
            backgroundColor: "hsl(var(--color-card))",
            border: "1px solid hsl(var(--color-border))",
            borderRadius: "8px",
          }}
          labelStyle={{ color: "hsl(var(--color-foreground))" }}
        />
        <Bar dataKey="priority" fill="hsl(var(--color-primary))" radius={[8, 8, 0, 0]} name="Priority Score" />
      </BarChart>
    </ResponsiveContainer>
  )
}
