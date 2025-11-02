"use client"

import { useState } from "react"
import Sidebar from "@/components/sidebar"
import Header from "@/components/header"
import Dashboard from "@/components/dashboard"
import InputTaskPage from "@/components/pages/input-task"
import TaskListPage from "@/components/pages/task-list"
import MLResultsPage from "@/components/pages/ml-results"
import SettingsPage from "@/components/pages/settings"
import AboutPage from "@/components/pages/about"

export default function Home() {
  const [sidebarOpen, setSidebarOpen] = useState(true)
  const [currentPage, setCurrentPage] = useState("dashboard")

  return (
    <div className="flex h-screen bg-background neural-bg">
      {/* Sidebar */}
      <Sidebar open={sidebarOpen} currentPage={currentPage} onNavigate={setCurrentPage} />

      {/* Main Content */}
      <div className="flex-1 flex flex-col overflow-hidden">
        {/* Header */}
        <Header sidebarOpen={sidebarOpen} onToggleSidebar={setSidebarOpen} />

        {/* Main Panel */}
        <main className="flex-1 overflow-auto">
          {currentPage === "dashboard" && <Dashboard />}
          {currentPage === "input" && <InputTaskPage />}
          {currentPage === "tasks" && <TaskListPage />}
          {currentPage === "results" && <MLResultsPage />}
          {currentPage === "settings" && <SettingsPage />}
          {currentPage === "about" && <AboutPage />}
        </main>
      </div>
    </div>
  )
}
