import { FiAlignJustify } from "react-icons/fi";
import { Link } from "react-router-dom";
export default function Navbar() {
    return(
        <nav className="p-6 md:p-8 flex justify-between items-center text-white md:w-full md:max-w-[1280px] md:mx-auto">
            <h1>
                Xcode
            </h1>
            <nav className="hidden md:flex">
                <ul className="flex md:gap-12">
                    <Link to='/'>Report Now</Link>
                    <Link to='/resources'>Resources</Link>
                    <Link to='/safetyTips'>Safety Tips</Link>
                </ul>
            </nav>
            <FiAlignJustify className="w-8 h-8 md:hidden"/>
        </nav>
    );
}