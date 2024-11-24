import { FiAlignJustify } from "react-icons/fi";

export default function Navbar() {
    return(
        <nav className="p-6 md:p-8 flex justify-between items-center text-white md:w-full md:max-w-[1280px] md:mx-auto">
            <h1>
                Xcode
            </h1>
            <nav className="hidden md:flex">
                <ul className="flex md:gap-12">
                    <li>Report Now</li>
                    <li>Resources</li>
                    <li>Safety Tips</li>
                </ul>
            </nav>
            <FiAlignJustify className="w-8 h-8 md:hidden"/>
        </nav>
    );
}