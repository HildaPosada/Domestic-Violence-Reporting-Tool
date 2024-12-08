// import { AiOutlineClose } from "react-icons/ai";

const NodalComponent = ({ open, onClose, children, className }) => {
  return (
    <div
      onClick={onClose}
      className={`fixed z-50 inset-0 flex justify-center items-center transition-colors ${
        open ? `backdrop-blur-none ${className || "bg-black/70"}` : "invisible"
      }`}
    >
      <div
        onClick={(e) => e.stopPropagation()}
        className={`
      bg-white w-full sm:max-w-md h-auto rounded-xl shadow p-4 transition-all ${
        open ? "scale-100 opacity-100 mx-4" : "scale-125 opacity-0"
      }`}
      >
        {/* <button
          type="button"
          onClick={onClose}
          className="absolute top-2 right-2 rounded-lg text-gray-400 bg-transparent text-2xl hover:bg-primary hover:text-gray-600"
        >
          <AiOutlineClose
            className="text-primary hover:text-white hover:rounded-lg"
            size={25}
          />
        </button> */}
        <div className="my-1">{children}</div>
      </div>
    </div>
  );
};

export default NodalComponent;
