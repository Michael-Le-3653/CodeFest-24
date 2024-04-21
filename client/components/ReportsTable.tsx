import React from 'react'
import prisma from '@/lib/prisma';
import { useEffect, useState } from 'react';
export default function ReportsTable ({data}) {
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
                            Description
                        </th>
                        <th scope="col" className="px-6 py-3">
                            Solution
                        </th>
                    </tr>
                </thead>
                <tbody>
                    {data.map((item, index) => (
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
                    ))}
                </tbody>
            </table>
        </div>
      
    </div>
  )
}
