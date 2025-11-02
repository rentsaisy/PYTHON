"use client"

import { Settings, Bell, Moon, Lock } from "lucide-react"
import { useState } from "react"

export default function SettingsPage() {
  const [settings, setSettings] = useState({
    notifications: true,
    darkMode: false,
    autoSave: true,
    privacy: "public",
  })

  return (
    <div className="min-h-screen p-4 md:p-8 bg-gradient-to-br from-background via-secondary/20 to-background neural-bg">
      <div className="max-w-2xl mx-auto space-y-8">
        {/* Header */}
        <div>
          <div className="flex items-center gap-3 mb-2">
            <div className="w-10 h-10 bg-gradient-to-br from-primary to-accent rounded-lg flex items-center justify-center shadow-md">
              <Settings className="w-6 h-6 text-foreground" />
            </div>
            <h1 className="text-4xl font-bold text-foreground">Settings</h1>
          </div>
          <p className="text-muted-foreground ml-13">Manage your preferences and account settings</p>
        </div>

        {/* Settings Sections */}
        <div className="space-y-6">
          {/* Notifications */}
          <div className="bg-card rounded-xl border border-border p-6">
            <div className="flex items-center gap-3 mb-4">
              <Bell className="w-5 h-5 text-primary" />
              <h3 className="font-semibold text-foreground">Notifications</h3>
            </div>
            <label className="flex items-center gap-3 cursor-pointer">
              <input
                type="checkbox"
                checked={settings.notifications}
                onChange={(e) => setSettings({ ...settings, notifications: e.target.checked })}
                className="w-4 h-4 rounded accent-primary"
              />
              <span className="text-muted-foreground">Enable task reminders</span>
            </label>
          </div>

          {/* Theme */}
          <div className="bg-card rounded-xl border border-border p-6">
            <div className="flex items-center gap-3 mb-4">
              <Moon className="w-5 h-5 text-primary" />
              <h3 className="font-semibold text-foreground">Appearance</h3>
            </div>
            <label className="flex items-center gap-3 cursor-pointer">
              <input
                type="checkbox"
                checked={settings.darkMode}
                onChange={(e) => setSettings({ ...settings, darkMode: e.target.checked })}
                className="w-4 h-4 rounded accent-primary"
              />
              <span className="text-muted-foreground">Dark Mode</span>
            </label>
          </div>

          {/* Privacy */}
          <div className="bg-card rounded-xl border border-border p-6">
            <div className="flex items-center gap-3 mb-4">
              <Lock className="w-5 h-5 text-primary" />
              <h3 className="font-semibold text-foreground">Privacy</h3>
            </div>
            <select className="w-full px-4 py-2 rounded-lg bg-input border border-border text-foreground focus:outline-none focus:ring-2 focus:ring-primary">
              <option>Public</option>
              <option>Private</option>
              <option>Friends Only</option>
            </select>
          </div>

          {/* Save Button */}
          <button className="w-full bg-gradient-to-r from-primary to-accent text-foreground font-semibold py-3 rounded-lg hover:shadow-lg smooth-transition">
            Save Settings
          </button>
        </div>
      </div>
    </div>
  )
}
