import React, { useEffect, useState} from 'react'
import Header from '@/components/Header'
import ReportsTable from '@/components/ReportsTable'
import prisma from '@/lib/prisma'

async function getReports() {
  const reports = await prisma.report.findMany({
    where: { published: true },
  });
  return reports;
}

export default function reports() {
  const [reportsData, setReportsData] = useState([]);

  useEffect(() => {
    const fetchReports = async () => {
      try {
        const reports = await getReports();
        setReportsData(reports);
      } catch (error) {
        console.error('Error fetching reports:', error);
      }
    };

    fetchReports();
  }, []);

  return (
    <>
      <Header/>
      <div className="bg-black flex flex-col h-screen px-10 py-5">
        <ReportsTable data={reportsData}/>
      </div>
    </>
  )
}

