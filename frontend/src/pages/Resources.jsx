import Navbar from "../components/Navbar";

export default function Resources() {
    return (
        <div className="h-full font-arimo">
            <section className="flex justify-center items-center h-[500px] md:h-[550px] mt-4 w-full">
                <div className="sm:[95%] w-4/5 max-w-[600px] bg-white px-6 pt-6 pb-8 rounded-lg shadow-custom relative">
                    <h2 className="text-xl md:text-3xl font-bold text-center">Resources</h2>
                    <ul className="list-disc mt-6 space-y-2 pl-5"> 
                        <li>
                            <a
                                href="https://www.thehotline.org/"
                                target="_blank"
                                rel="noopener noreferrer"
                                className="text-blue-600 hover:underline"
                            >
                                National Domestic Violence Hotline
                            </a>
                        </li>
                        <li>
                            <a
                                href="https://www.rainn.org/"
                                target="_blank"
                                rel="noopener noreferrer"
                                className="text-blue-600 hover:underline"
                            >
                                RAINN (Rape, Abuse & Incest National Network)
                            </a>
                        </li>
                        <li>
                            <a
                                href="https://www.samhsa.gov/"
                                target="_blank"
                                rel="noopener noreferrer"
                                className="text-blue-600 hover:underline"
                            >
                                SAMHSA (Substance Abuse and Mental Health Services Administration)
                            </a>
                        </li>
                    </ul>
                </div>
            </section>
        </div>
    );
}
