import { useState, useRef } from "react";
import { IoIosAddCircle, IoIosRemoveCircle } from "react-icons/io";
import { IoMicOutline } from "react-icons/io5";
import { CiFileOn } from "react-icons/ci";

export default function Home() {
    const [reportId, setReportId] = useState(""); // State for the Report ID
    const [upload, setUpload] = useState(false); // State for toggling upload options
    const [audioBlob, setAudioBlob] = useState(null); // State for audio Blob
    const [file, setFile] = useState(null); // State for uploaded file
    const mediaRecorder = useRef(null); // Ref for MediaRecorder
    const [recording, setRecording] = useState(false); // State for recording status

    const handleUploadState = () => {
        setUpload(!upload); // Toggle upload options
    };

    const handleFileUpload = (e) => {
        const selectedFile = e.target.files[0];
        if (selectedFile) {
            setFile(selectedFile);
        }
    };

    const handleStartRecording = async () => {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
            mediaRecorder.current = new MediaRecorder(stream);
            const chunks = [];

            mediaRecorder.current.ondataavailable = (e) => {
                chunks.push(e.data);
            };

            mediaRecorder.current.onstop = () => {
                const audio = new Blob(chunks, { type: "audio/ogg; codecs=opus" });
                setAudioBlob(audio);
            };

            mediaRecorder.current.start();
            setRecording(true);
        } catch (error) {
            console.error("Error accessing microphone:", error);
        }
    };

    const handleStopRecording = () => {
        if (mediaRecorder.current) {
            mediaRecorder.current.stop();
        }
        setRecording(false);
    };

    const handleSubmit = async (e) => {
        e.preventDefault(); // Prevent page refresh
        const userId = e.target.userId.value; // Grab User ID from input box
        const description = e.target.description.value; // Grab description from textarea
        const agency_id = "3fa85f64-5717-4562-b3fc-2c963f66afa6"; // Replace with a valid agency ID

        // Create a FormData object for submission
        const formData = new FormData();
        formData.append("userId", userId);
        formData.append("description", description);
        formData.append("agency_id", agency_id);

        // Attach the selected file, if any
        if (file) {
            formData.append("file", file);
        }

        // Attach the recorded audio, if any
        if (audioBlob) {
            formData.append("audio", audioBlob, "recording.ogg");
        }

        try {
            const response = await fetch(
                "https://domestic-violence-reporting-tool-m1sd.onrender.com/api/v1/reports/create-anonymous",
                {
                    method: "POST",
                    body: formData,
                }
            );

            if (response.ok) {
                const data = await response.json(); // Parse backend response
                setReportId(data.reportId); // Save the Report ID
                console.log("Report successfully created with ID:", data.reportId);
            } else {
                const errorData = await response.json();
                console.error("Failed to submit report:", errorData.message || response.statusText);
            }
        } catch (error) {
            console.error("Error submitting report:", error);
        }
    };

    return (
        <div className="flex justify-center items-center h-[500px] md:h-[550px] mt-4 w-full">
            <form
                onSubmit={handleSubmit}
                className="sm:w-[95%] w-4/5 max-w-[600px] bg-white px-6 pt-6 pb-8 rounded-lg shadow-custom relative"
            >
                <h2 className="text-xl md:text-3xl font-bold text-center">Domestic Violence</h2>

                {/* User ID Input Box */}
                <div className="input-box mt-5">
                    <label htmlFor="userId" className="block font-medium">
                        User ID
                    </label>
                    <input
                        type="text"
                        id="userId"
                        name="userId"
                        placeholder="Enter username"
                        className="w-full h-[40px] border-2 border-solid border-gray-300 outline-none rounded-md p-4 md:text-base text-sm text-gray-700 mt-1"
                        required
                    />
                </div>

                {/* Description Box */}
                <div className="input-box mt-7 mb-9">
                    <label htmlFor="description" className="block font-medium">
                        What happened?
                    </label>
                    <textarea
                        id="description"
                        name="description"
                        placeholder="Describe the incident..."
                        className="w-full h-[200px] border-2 border-solid border-gray-300 outline-none rounded-md p-4 md:text-base text-sm text-gray-700 mt-2 resize-none"
                        required
                    ></textarea>
                </div>

                {/* Upload Section */}
                <div className="flex justify-between items-center">
                    {/* Upload Button */}
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

                    {/* Report History Button */}
                    <button
                        type="button"
                        className="h-[40px] px-4 bg-blue-500 text-white rounded-md shadow hover:bg-blue-600 transition"
                        onClick={() => (window.location.href = "/follow-up-reports")}
                    >
                        Follow-Up Reports
                    </button>
                </div>

                <div
                    className={`bg-blue-600 w-44 rounded-md h-20 flex justify-center items-start flex-col py-6 pl-2 gap-2 text-white absolute bottom-44 left-14 transform transition-all duration-500 ease-in-out ${
                        upload ? "opacity-100 scale-100" : "opacity-0 scale-95 pointer-events-none"
                    }`}
                >
                    {!recording ? (
                        <button type="button" className="flex gap-1 items-center" onClick={handleStartRecording}>
                            <IoMicOutline className="w-6 h-6" />
                            <p className="text-[15px] leading-5">Record Voice</p>
                        </button>
                    ) : (
                        <button type="button" className="flex gap-1 items-center" onClick={handleStopRecording}>
                            <IoMicOutline className="w-6 h-6 text-red-500" />
                            <p className="text-[15px] leading-5">Stop Recording</p>
                        </button>
                    )}

                    <input
                        type="file"
                        accept="image/*,video/*"
                        onChange={handleFileUpload}
                        className="hidden"
                        id="fileInput"
                    />
                    <label htmlFor="fileInput" className="flex gap-1 items-center cursor-pointer">
                        <CiFileOn className="w-6 h-6" />
                        <p className="text-[15px] leading-5">Upload a file</p>
                    </label>
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
