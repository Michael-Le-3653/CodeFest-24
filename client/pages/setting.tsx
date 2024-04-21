import React from 'react'
import Header from '@/components/Header'
import UserSettings from '@/components/UserSettings'
export default function reports() {
  return (
    <>
      <Header/>
      <div className="bg-black flex flex-col h-screen px-10 py-5">
        <UserSettings/>
      </div>
    </>
  )
}
