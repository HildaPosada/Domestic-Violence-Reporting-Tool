import Navbar from "../components/Navbar";

export default function SafetyTips() {
    return(
        <div className="bg-gradient-to-b from-custom-blue to-custom-purple h-screen font-arimo">
            <Navbar/>
            <section className="flex justify-center items-center h-[500px] md:h-[550px] mt-12 w-full">
                <div className="sm:[95%] w-4/5 max-w-[600px] bg-white px-6 pt-6 pb-8 rounded-lg h-full shadow-custom ">
                <h2 className="text-xl md:text-3xl font-bold text-center">Safety Tips</h2>
                </div>
            </section>
        </div>
    );
}