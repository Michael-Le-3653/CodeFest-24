import React from 'react'
import Header from '@/components/Header'
import ReportsTable from '@/components/ReportsTable'
export default function reports() {
  return (
    <>
      <Header/>
      <div className="bg-black flex flex-col h-screen px-10 py-5">
        <ReportsTable/>
      </div>
    </>
  )
}
