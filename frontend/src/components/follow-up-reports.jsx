import { useState } from "react";

export default function FollowUpReports() {
    const [userId, setUserId] = useState(""); // State for User ID
    const [reportId, setReportId] = useState(""); // State for specific Report ID
    const [reports, setReports] = useState([]); // State for reports history
    const [reportDetails, setReportDetails] = useState(null); // State for specific report details
    const [loading, setLoading] = useState(false); // State for loading

    // Fetch report history by User ID
    const fetchReports = async () => {
        setLoading(true);
        try {
            const response = await fetch(
                `https://domestic-violence-reporting-tool-m1sd.onrender.com/api/v1/reports/get-all-user-reports/${userId}`
            );

            if (response.ok) {
                const data = await response.json();
                setReports(data);
            } else {
                console.error("Failed to fetch reports");
                setReports([]);
            }
        } catch (error) {
            console.error("Error fetching reports:", error);
        } finally {
            setLoading(false);
        }
    };

    // Fetch specific report details by Report ID
    const fetchReportDetails = async () => {
        setLoading(true);
        try {
            const response = await fetch(
                `https://domestic-violence-reporting-tool-m1sd.onrender.com/api/v1/reports/get-all-follow-up-reports/${reportId}`
            );

            if (response.ok) {
                const data = await response.json();
                setReportDetails(data);
            } else {
                console.error("Failed to fetch report details");
                setReportDetails(null);
            }
        } catch (error) {
            console.error("Error fetching report details:", error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="flex justify-center items-center flex-col h-screen p-6">
            <h2 className="text-2xl font-bold mb-6">Follow-Up Reports</h2>

            {/* Input for User ID */}
            <div className="w-full max-w-md mb-6">
                <label htmlFor="userId" className="block font-medium mb-2">
                    Enter User ID
                </label>
                <input
                    type="text"
                    id="userId"
                    value={userId}
                    onChange={(e) => setUserId(e.target.value)}
                    placeholder="Enter your User ID"
                    className="w-full h-[40px] border-2 border-solid border-gray-300 outline-none rounded-md p-2 text-gray-700"
                />
                <button
                    onClick={fetchReports}
                    className="w-full mt-4 h-[40px] bg-blue-500 text-white rounded-md hover:bg-blue-600 transition"
                >
                    {loading ? "Loading..." : "Fetch Report History"}
                </button>
            </div>

            {/* Display Report History */}
            <div className="w-full max-w-2xl">
                {reports.length > 0 && (
                    <div>
                        <h3 className="text-lg font-bold mb-4">Report History</h3>
                        <ul className="list-disc pl-5">
                            {reports.map((report) => (
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
                    onClick={fetchReportDetails}
                    className="w-full mt-4 h-[40px] bg-blue-500 text-white rounded-md hover:bg-blue-600 transition"
                >
                    {loading ? "Loading..." : "Fetch Report Details"}
                </button>
            </div>

            {/* Display Specific Report Details */}
            {reportDetails && (
                <div className="w-full max-w-2xl mt-6">
                    <h3 className="text-lg font-bold mb-4">Report Details</h3>
                    <ul className="list-disc pl-5">
                        {reportDetails.map((followUp) => (
                            <li key={followUp.follow_up_id} className="mb-2">
                                <strong>Description:</strong> {followUp.description} <br />
                                <strong>Date:</strong> {new Date(followUp.date_created).toLocaleString()}
                            </li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
}
