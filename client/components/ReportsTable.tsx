import React from 'react'

// async function getReports (){
//   const reports = await prisma.report.findMany({
//     where: {published:true},
//   })
//   return reports
// }

export default function ReportsTable(){
  return (
    <div>
        <div className="relative overflow-x-auto">
            <table className="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                    <tr>
                        <th scope="col" className="px-6 py-3">
                            Date
                        </th>
                        <th scope="col" className="px-6 py-3">
                            Title
                        </th>
                        <th scope="col" className="px-6 py-3">
                            Technical Device
                        </th>
                        <th scope="col" className="px-6 py-3">
                            Device ID
                        </th>
                        <th scope="col" className="px-6 py-3">
                            Description
                        </th>
                        <th scope="col" className="px-6 py-3">
                            Solution
                        </th>
                        <th scope="col" className="px-6 py-3">
                            Priority
                        </th>
                        <th scope="col" className="px-6 py-3">
                            Location
                        </th>
                    </tr>
                </thead>
                <tbody>
                {/* {reports && reports.map((item) => (
                    <tr className="bg-white border-b dark:bg-gray-800 dark:border-gray-700" key={index}>
                        <th scope="row" className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            {item.date}
                        </th>
                        <td className="px-6 py-4">
                            {item.title}
                        </td>
                        <td className="px-6 py-4">
                            {item.device}
                        </td>
                        <td className="px-6 py-4">
                            {item.description}
                        </td>
                        <td className="px-6 py-4">
                            {item.solution}
                        </td>
                    </tr>
                      ))} */}
                    <tr className="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                        <th scope="row" className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                           April, 21, 2024 3:00 PM
                        </th>
                        <td className="px-6 py-4">
                            Xfinity TV Broken Screen
                        </td>
                        <td className="px-6 py-4">
                            Xfinity TV
                        </td>
                        <td className="px-6 py-4">
                            12345689
                        </td>
                        <td className="px-6 py-4">
                            XFinity TV is not streaming movies
                        </td>
                        <td className="px-6 py-4">
                           Comcast Center technican will take a look.
                        </td>
                        <td className="px-6 py-4">
                           High
                        </td>
                        <td className="px-6 py-4">
                           Philadelphia, PA
                        </td>
                    </tr>
                    <tr className="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                        <th scope="row" className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                           April, 31, 2024 5:15 PM
                        </th>
                        <td className="px-6 py-4">
                            xFi Wi-Fi Connection
                        </td>
                        <td className="px-6 py-4">
                            xFi Advanced Gateway
                        </td>
                        <td className="px-6 py-4">
                            12345683
                        </td>
                        <td className="px-6 py-4">
                            xFi Advanced Gateway is displaying low signal
                        </td>
                        <td className="px-6 py-4">
                           Comcast Center technican will send a new xFi Advanced Gateway
                        </td>
                        <td className="px-6 py-4">
                           Moderate
                        </td>
                        <td className="px-6 py-4">
                           Philadelphia, PA
                        </td>
                    </tr>
                    <tr className="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                        <th scope="row" className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                           April, 31, 2024 3:00 PM
                        </th>
                        <td className="px-6 py-4">
                            X1 remote voice detection 
                        </td>
                        <td className="px-6 py-4">
                            X1 Voice Remote
                        </td>
                        <td className="px-6 py-4">
                            15345689
                        </td>
                        <td className="px-6 py-4">
                            X1 Voice Remote is not detecting commands in Spanish
                        </td>
                        <td className="px-6 py-4">
                           Will send a call back to confirm this is not a widespread issue
                        </td>
                        <td className="px-6 py-4">
                           High
                        </td>
                        <td className="px-6 py-4">
                           Philadelphia, PA
                        </td>
                    </tr>
                    <tr className="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                        <th scope="row" className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                           March 21, 2024 3:00 PM
                        </th>
                        <td className="px-6 py-4">
                            X-Cam Quality 
                        </td>
                        <td className="px-6 py-4">
                            X-Cam 
                        </td>
                        <td className="px-6 py-4">
                            12343021
                        </td>
                        <td className="px-6 py-4">
                            X-Cam graphics is blurry
                        </td>
                        <td className="px-6 py-4">
                           Will troubleshoot AI integration
                        </td>
                        <td className="px-6 py-4">
                           High
                        </td>
                        <td className="px-6 py-4">
                           Philadelphia, PA
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
      
    </div>
  )
}
