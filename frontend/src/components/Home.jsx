import { useState, useRef } from "react";
import { IoIosAddCircle, IoIosRemoveCircle, IoMdCheckmark } from "react-icons/io";
import { IoMicOutline } from "react-icons/io5";
import { CiFileOn } from "react-icons/ci";
import { useNavigate } from "react-router-dom"; // For navigation
import NodalComponent from "./Modal";

export default function Home() {
  const navigate = useNavigate(); // Hook for programmatic navigation

  const [notification, setNotification] = useState(false);
  const [loading, setLoading] = useState(false);
  const [reportData, setReportData] = useState({
    username: "",
    description: "",
  }); // State for the Report ID
  const [reportId, setReportId] = useState("")

  const handleSubmit = async (e) => {
    setLoading(true);
    setNotification(false)
    e.preventDefault(); // Prevent page refresh
    // const userId = e.target.userId.value; // Grab User ID from input box
    // const description = e.target.description.value; // Grab description from textarea
    const agency_id = "3fa85f64-5717-4562-b3fc-2c963f66afa6"; // Replace with a valid agency ID

    // Create a FormData object for submission
    // const formData = new FormData();
    // formData.append("username", reportData.username);
    // formData.append("description", reportData.description);
    // formData.append("agency_id", agency_id);

    // // Attach the selected file, if any
    // if (file) {
    //   formData.append("file", file);
    // }

    // // Attach the recorded audio, if any
    // if (audioBlob) {
    //   formData.append("audio", audioBlob, "recording.ogg");
    // }

    let formData = {
      ...reportData,
      agency_id,
    };

    try {
      const response = await fetch(
        `${import.meta.env.VITE_BACKEND_API}/api/v1/reports/create-report`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json", // Add Content-Type header
          },
          body: JSON.stringify(formData),
        }
      );

      if (response.ok) {
        const data = await response.json(); // Parse backend response

        setReportId(data.reportId)
        setNotification(true)
        setLoading(false);
      } else {
        const errorData = await response.json();
        console.error(
          "Failed to submit report:",
          errorData.message || response.statusText
        );
        setLoading(false);
      }
    } catch (error) {
      console.error("Error submitting report:", error);

      setLoading(false);
    }
  };

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

  return (
    <div className="flex justify-center pt-4 w-full">
      <div className="flex flex-col justify-center items-center">
        <form
          onSubmit={handleSubmit}
          className="w-full sm:min-w-[500px] max-w-[600px] bg-white px-6 pt-6 pb-8 rounded-lg shadow-custom relative"
        >
          <h2 className="text-xl md:text-3xl font-bold text-center">
            Domestic Violence
          </h2>

          {/* User ID Input Box */}
          <div className="input-box mt-5">
            <label htmlFor="userId" className="block font-medium">
              Username <span className="text-gray-500">(Optional)</span>
            </label>
            <input
              onChange={(e) =>
                setReportData({
                  ...reportData,
                  username: e.target.value,
                })
              }
              type="text"
              id="username"
              name="username"
              placeholder="Enter username"
              className="w-full h-[40px] border-2 border-solid border-gray-300 outline-none rounded-md p-4 md:text-base text-sm text-gray-700 mt-1"
            />
          </div>

          {/* Description Box */}
          <div className="input-box mt-7 mb-9">
            <label htmlFor="description" className="block font-medium">
              What happened?
            </label>
            <textarea
              onChange={(e) =>
                setReportData({
                  ...reportData,
                  description: e.target.value,
                })
              }
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
              {/* <p>Upload</p> */}
            </div>

            {/* Follow-Up Reports Button */}
            <button
              type="button"
              className="px-4 py-1 md:py-2 bg-blue-500 text-white rounded-md shadow hover:bg-blue-600 transition-all ease-in-out duration-300"
              onClick={() => navigate("/follow-up-reports")}
            >
              Report History
            </button>
          </div>

          <div
            className={`bg-blue-600 w-44 rounded-md h-20 flex justify-center items-start flex-col py-6 pl-2 gap-2 text-white absolute bottom-44 left-14 transform transition-all duration-500 ease-in-out ${
              upload
                ? "opacity-100 scale-100"
                : "opacity-0 scale-95 pointer-events-none"
            }`}
          >
            {!recording ? (
              <button
                type="button"
                className="flex gap-1 items-center"
                onClick={handleStartRecording}
              >
                <IoMicOutline className="w-6 h-6" />
                <p className="text-[15px] leading-5">Record Voice</p>
              </button>
            ) : (
              <button
                type="button"
                className="flex gap-1 items-center"
                onClick={handleStopRecording}
              >
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
            <label
              htmlFor="fileInput"
              className="flex gap-1 items-center cursor-pointer"
            >
              <CiFileOn className="w-6 h-6" />
              <p className="text-[15px] leading-5">Upload a file</p>
            </label>
          </div>

          {/* Submit Button */}
          <button
            type="submit"
            className="py-2 md:py-3 w-full bg-purple-500 border-none rounded-md shadow-custom cursor-pointer text-base mt-8 text-white hover:bg-purple-600 transition"
          >
            {loading ? (
              <span className="animate-pulse">Submitting....</span>
            ) : (
              "Submit Report!"
            )}
          </button>

          {/* Show the Report ID if it exists */}
        </form>

        

          {/* )} */}
          <NodalComponent
            open={notification}
            onClose={() => setNotification(false)}
          >
            <div className="flex items-center flex-col gap-4">
              <span className="p-2 bg-green-500 rounded-full"><IoMdCheckmark size={20} color="white" /></span>
              <p className="text-green-600 text-center">
                Thank you! Your report has been submitted. Your Report ID is:{" "}
                <strong>{reportId}</strong>. Please keep this for reference.
              </p>
              <button onClick={() => setNotification(false)} type="button" className=" px-2 py-1.5 bg-red-500 text-white rounded w-max">Close</button>
            </div>
          </NodalComponent>
  
      </div>
    </div>
  );
}
