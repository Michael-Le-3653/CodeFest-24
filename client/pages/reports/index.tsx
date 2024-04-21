import React, { useEffect, useState} from 'react'
import Header from '@/components/Header'
import ReportsTable from '@/components/ReportsTable'
import prisma from '@/lib/prisma'

// async function getReports (){
//   const reports = await prisma.report.findMany({
//     where: {published:true},
//   })
//   return reports
// }

export default function reports() {
  //const reports = await getReports();
  // console.log({reports})
  return (
    <>
      <Header/>
      <div className="bg-black flex flex-col h-screen px-10 py-5">
        <ReportsTable/>
      </div>
    </>
  )
}

