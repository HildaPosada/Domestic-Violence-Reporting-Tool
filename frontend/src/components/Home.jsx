import { IoIosAddCircle, IoIosRemoveCircle  } from "react-icons/io";
import { IoMicOutline } from "react-icons/io5";
import { CiFileOn } from "react-icons/ci";
import { useState } from 'react'

export default function Home() {
    const [upload, setUpload] = useState(false);

    function handleUploadState() {
        setUpload(!upload)
    }

    return(
        <section className="home flex justify-center items-center h-[500px] md:h-[550px] mt-8 w-full">
            <form action="" className="sm:[95%] w-4/5 max-w-[600px] bg-white px-6 pt-6 pb-8 rounded-lg h-full shadow-custom relative">
                <h2 className="text-xl md:text-3xl font-bold text-center">Domestic Violence</h2>
                <div className="input-box mt-7 mb-9">
                    <label>What happened?</label>
                    <textarea name="" id="" placeholder="Describe the incident..." className="w-full h-[200px] border-2 border-solid border-[#ddd] outline-none rounded-md p-4 md:text-base text-sm text-gray-500 mt-2 resize-none"></textarea>
                    <div className="flex items-center gap-1 text-sm w-20 transform transition-all duration-500 ease-in-out md:mt-4" onClick={handleUploadState}> 
                        { upload ? <IoIosRemoveCircle className="bg-white rounded-full text-[#5935e4] h-7 w-7 transition-all duration-500 ease-in-out" /> : <IoIosAddCircle className="bg-white rounded-full text-[#5935e4] h-7 w-7 transition-all duration-500 ease-in-out"/>}
                         <p>Upload</p>
                    </div>
                    <hr className="mb-3 mt-2" />
                </div>

                <div className={`bg-[#4467eb] w-44 rounded-md h-20 flex justify-center items-start flex-col py-6 pl-2 gap-2 text-white absolute bottom-44 left-14 transform transition-all duration-500 ease-in-out ${upload ? 'opacity-100 scale-100' : 'opacity-0 scale-95 pointer-events-none'}`}>
                    <button className="flex gap-1 items-center">
                        <IoMicOutline className="w-6 h-6"/>
                        <p className="text-[15px] leading-5">Voice message</p>
                    </button>
                    <button className="flex
                    gap-1 items-center">
                        <CiFileOn className="w-6 h-6"/>
                        <p className="text-[15px] leading-5">Upload a file</p>
                    </button>
                </div>
                <button type="submit" className="w-full h-14 bg-[#826afb] border-none rounded-md shadow-custom cursor-pointer text-base md:mt-8 mt-4 text-white">Submit Report!</button>
            </form>
        </section>
    );
}