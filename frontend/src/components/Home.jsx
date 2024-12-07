import { useState } from "react";
import { IoIosAddCircle, IoIosRemoveCircle } from "react-icons/io";
import { IoMicOutline } from "react-icons/io5";
import { CiFileOn } from "react-icons/ci";

export default function Home() {
    const [reportId, setReportId] = useState(""); // State for the Report ID
    const [upload, setUpload] = useState(false); // State for toggling upload options

    const handleUploadState = () => {
        setUpload(!upload); // Toggle upload options
    };

    const handleSubmit = async (e) => {
        e.preventDefault(); // Prevent page refresh
        const description = e.target.description.value; // Grab description from textarea

        try {
            const response = await fetch("https://your-backend-url.onrender.com/api/reports", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ description }), // Send description as JSON
            });

            if (response.ok) {
                const data = await response.json(); // Parse backend response
                setReportId(data.reportId); // Save the Report ID
            } else {
                console.error("Failed to submit report");
            }
        } catch (error) {
            console.error("Error submitting report:", error);
        }
    };

    return (
        <div className="flex flex-col justify-center items-center min-h-screen bg-gradient-to-b from- to-">

            {/* Form Container */}
            <form
                onSubmit={handleSubmit}
                className="sm:w-[95%] w-4/5 max-w-[600px] bg-white px-6 pt-6 pb-8 rounded-lg shadow-custom relative"
            >
                <h2 className="text-xl md:text-3xl font-bold text-center">Domestic Violence</h2>
                <div className="input-box mt-7 mb-9">
                    <label htmlFor="description" className="block font-medium">
                        What happened?
                    </label>
                    <textarea
                        id="description"
                        name="description"
                        placeholder="Describe the incident..."
                        className="w-full h-[200px] border-2 border-solid border-gray-300 outline-none rounded-md p-4 md:text-base text-sm text-gray-700 mt-2 resize-none"
                    ></textarea>
                </div>

                {/* Upload Section */}
                <div
                    className="flex items-center gap-1 text-sm w-20 transform transition-all duration-500 ease-in-out cursor-pointer"
                    onClick={handleUploadState}
                >
                    {upload ? (
                        <IoIosRemoveCircle className="bg-white rounded-full text-purple-700 h-7 w-7 transition-all duration-500 ease-in-out" />
                    ) : (
                        <IoIosAddCircle className="bg-white rounded-full text-purple-700 h-7 w-7 transition-all duration-500 ease-in-out" />
                    )}
                    <p>Upload</p>
                </div>
                <div
                    className={`bg-blue-600 w-44 rounded-md h-20 flex justify-center items-start flex-col py-6 pl-2 gap-2 text-white absolute bottom-44 left-14 transform transition-all duration-500 ease-in-out ${
                        upload ? "opacity-100 scale-100" : "opacity-0 scale-95 pointer-events-none"
                    }`}
                >
                    <button className="flex gap-1 items-center">
                        <IoMicOutline className="w-6 h-6" />
                        <p className="text-[15px] leading-5">Voice message</p>
                    </button>
                    <button className="flex gap-1 items-center">
                        <CiFileOn className="w-6 h-6" />
                        <p className="text-[15px] leading-5">Upload a file</p>
                    </button>
                </div>

                {/* Submit Button */}
                <button
                    type="submit"
                    className="w-full h-14 bg-purple-500 border-none rounded-md shadow-custom cursor-pointer text-base mt-8 text-white hover:bg-purple-600 transition"
                >
                    Submit Report!
                </button>

                {/* Show the Report ID if it exists */}
                {reportId && (
                    <p className="mt-4 text-green-600">
                        Thank you! Your report has been submitted. Your Report ID is: <strong>{reportId}</strong>
                    </p>
                )}
            </form>
        </div>
    );
}
