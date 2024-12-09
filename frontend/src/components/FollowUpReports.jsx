import { useState } from "react";

export default function FollowUpReports() {
    const [username, setUsername] = useState(""); // State for User ID
    const [reportId, setReportId] = useState(""); // State for specific Report ID
    const [reportsByUsername, setReportsByUsername] = useState([]); // State for reports history
    const [reportsById, setReportsById] = useState([]); // State for specific report details
    const [loadingByUsername, setLoadingByUsername] = useState(false); // State for loading
    const [loadingByByReportId, setLoadingByByReportId] = useState(false); // State for loading

    // Fetch report history by User ID
    const fetchReportsByUsername = async () => {
        setLoadingByUsername(true);
        try {
            const response = await fetch(
                `${import.meta.env.VITE_BACKEND_API}/api/v1/reports/${username}`
            );

            if (response.ok) {
                const data = await response.json();
                setReportsByUsername(data);
            } else {
                console.error("Failed to fetch reports");
                setReportsByUsername([]);
            }
        } catch (error) {
            console.error("Error fetching reports:", error);
        } finally {
            setLoadingByUsername(false);
        }
    };

    // Fetch specific report details by Report ID
    const fetchReportById = async () => {
        setLoadingByByReportId(true);
        try {
            const response = await fetch(
                `${import.meta.env.VITE_BACKEND_API}/api/v1/reports/report/${reportId}`
            );

            if (response.ok) {
                const data = await response.json();
                setReportsById(data);
            } else {
                console.error("Failed to fetch report details");
                setReportsById([]);
            }
        } catch (error) {
            console.error("Error fetching report details:", error);
        } finally {
            setLoadingByByReportId(false);
        }
    };

    console.log(reportsByUsername)

    console.log(reportsById)

    return (
        <div className="bg-gradient-to-b from-custom-blue to-custom-purple flex justify-center items-center flex-col h-screen p-6">
            <div className="bg-white p-4 md:p-6 rounded-lg">
                <h2 className="text-2xl font-bold mb-6">Report History</h2>

                {/* Input for User ID */}
                <div className="w-full max-w-md mb-6">
                    <label htmlFor="username" className="block font-medium mb-2">
                        Enter Username
                    </label>
                    <input
                        type="text"
                        id="username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        placeholder="Enter your User ID"
                        className="w-full h-[40px] border-2 border-solid border-gray-300 outline-none rounded-md p-2 text-gray-700"
                    />
                    <button
                        onClick={fetchReportsByUsername}
                        className="w-full mt-4 h-[40px] bg-blue-500 text-white rounded-md hover:bg-blue-600 transition"
                    >
                        {loadingByUsername ? "Loading..." : "Fetch Report History"}
                    </button>
                </div>

                {/* Display Report History */}
                <div className="w-full max-w-md mb-6 overflow-y-auto">
                    {reportsByUsername && reportsByUsername.length > 0 && (
                        <div>
                            <h3 className="text-lg font-bold mb-4">Report History</h3>
                            <ul className="list-disc pl-5">
                                {reportsByUsername.map((report) => (
                                    <li key={report.report_id} className="mb-2">
                                        <strong>Report ID:</strong> {report.report_id} <br />
                                        <strong>Time:</strong> {new Date(report.date_created).toLocaleString()} <br />
                                        <strong>Progress:</strong> {report.progress || "In Progress"}
                                    </li>
                                ))}
                            </ul>
                        </div>
                    )}
                </div>

                {/* Input for Specific Report ID */}
                <div className="w-full max-w-md mt-8">
                    <label htmlFor="reportId" className="block font-medium mb-2">
                        Enter Report ID
                    </label>
                    <input
                        type="text"
                        id="reportId"
                        value={reportId}
                        onChange={(e) => setReportId(e.target.value)}
                        placeholder="Enter Report ID"
                        className="w-full h-[40px] border-2 border-solid border-gray-300 outline-none rounded-md p-2 text-gray-700"
                    />
                    <button
                        onClick={fetchReportById}
                        className="w-full mt-4 h-[40px] bg-blue-500 text-white rounded-md hover:bg-blue-600 transition"
                    >
                        {loadingByByReportId ? "Loading..." : "Fetch Report Details"}
                    </button>
                </div>

                {/* Display Specific Report Details */}
                <div className="w-full max-w-md mt-8 overflow-y-auto">
                    {reportsById && reportsById.length > 0 && (
                        <div>
                            <h3 className="text-lg font-bold mb-4">Report History</h3>
                            <ul className="list-disc pl-5">
                                {reportsById.map((report) => (
                                    <li key={report.report_id} className="mb-2">
                                        <strong>Report ID:</strong> {report.report_id} <br />
                                        <strong>Time:</strong> {new Date(report.date_created).toLocaleString()} <br />
                                        <strong>Progress:</strong> {report.progress || "In Progress"}
                                    </li>
                                ))}
                            </ul>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
}
