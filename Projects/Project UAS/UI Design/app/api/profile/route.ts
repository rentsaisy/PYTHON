import { NextRequest, NextResponse } from 'next/server'
import pool from '@/lib/db'

// GET profile by user ID (for now using ID 1 as default user)
export async function GET() {
  try {
    const [rows]: any = await pool.query(
      'SELECT * FROM users WHERE id = ?',
      [1]
    )
    
    if (rows.length === 0) {
      return NextResponse.json({ name: 'Student', image: null }, { status: 200 })
    }
    
    return NextResponse.json(rows[0], { status: 200 })
  } catch (error) {
    console.error('Database error:', error)
    return NextResponse.json(
      { error: 'Failed to fetch profile' },
      { status: 500 }
    )
  }
}

// POST/PUT update profile
export async function POST(request: NextRequest) {
  try {
    const body = await request.json()
    const { name, image } = body
    
    // Check if user exists
    const [rows]: any = await pool.query(
      'SELECT * FROM users WHERE id = ?',
      [1]
    )
    
    if (rows.length === 0) {
      // Insert new user
      await pool.query(
        'INSERT INTO users (id, name, image) VALUES (?, ?, ?)',
        [1, name, image]
      )
    } else {
      // Update existing user
      await pool.query(
        'UPDATE users SET name = ?, image = ? WHERE id = ?',
        [name, image, 1]
      )
    }
    
    return NextResponse.json({ success: true, name, image }, { status: 200 })
  } catch (error) {
    console.error('Database error:', error)
    return NextResponse.json(
      { error: 'Failed to update profile' },
      { status: 500 }
    )
  }
}
