import { useForm } from "react-hook-form";
import { useState } from "react";

export default function Registration() {
  const [navigate, setNavigate] = useState(false);
  const [loading, setLoading] = useState(false)

  async function handleFormNavigation() {
    if (!navigate) {
      const isValid = await trigger(["agency_name", "email"]); // Validate first-page fields
      if (isValid) setNavigate((nav) => !nav); // Only navigate if valid
    } else {
      setNavigate((nav) => !nav); // Allow navigation back without validation
    }
  }

  async function handleFormSubmit(data) {
    try {
      const response = await fetch(
        `${import.meta.env.VITE_BACKEND_API}/api/v1/reports/create-report`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json", // Add Content-Type header
          },
          body: JSON.stringify(data),
        }
      );

      if (response.ok) {
        const data = await response.json(); // Parse backend response

        
        setLoading(false);
      } else {
        const errorData = await response.json();
        console.error(
          "Failed to submit report:",
          errorData.message || response.statusText
        );
        setLoading(false);
        setReportData(initialReportData)
      }
    } catch (error) {
      console.error("Error submitting report:", error);
      setReportData(initialReportData)
      setLoading(false);
    }
  };

  const {
    register,
    handleSubmit,
    formState: { errors },
    trigger,
  } = useForm();

  return (
    <div className="bg-gradient-to-b from-custom-blue to-custom-purple h-screen font-arimo flex justify-center items-center">
      <div className="w-4/5 md:max-w-[600px] bg-white h-[500px] rounded-md flex flex-col items-center">
        <h2 className="text-xl md:text-2xl font-bold text-center mt-8 ">
          Agency Registration
        </h2>
        <form
          className="w-full max-w-[550px] bg-white px-3 md:px-8 pt-6 flex flex-col mt-4"
          onSubmit={handleSubmit(handleFormSubmit)}
          autoComplete="on"
        >
          <div
            className={
              navigate
                ? "opacity-0 hidden pointer-events-none"
                : "flex flex-col gap-6 opacity-100"
            }
          >
            <label htmlFor="agencyName">
              <div className="flex justify-between items-center">
                <span className="font-medium block">Agency Name</span>
                {errors.agency_name && (
                  <p className="text-red-500 text-sm">{errors.agency_name.message}</p>
                )}
              </div>
              <input
                {...register("agency_name", {
                  required: "Required",
                })}
                type="text"
                className="w-full h-[40px] border-2 border-solid border-gray-300 outline-none rounded-md p-4 md:text-base text-sm text-gray-700 mt-1"
                placeholder="Agency name"
                id="agencyName"
              />
            </label>
            <label htmlFor="email">
              <div className="flex justify-between items-center">
                <span className="font-medium block">Email</span>
                {errors.email && (
                  <p className="text-red-500 text-sm">{errors.email.message}</p>
                )}
              </div>
              <input
                {...register("email", {
                  required: "This is a required field",
                  maxLength: {
                    value: 254,
                    message: "Character limit exceeded",
                  },
                })}
                type="email"
                className="w-full h-[40px] border-2 border-solid border-gray-300 outline-none rounded-md p-4 md:text-base text-sm text-gray-700 mt-1"
                placeholder="johndoe@gmail.com"
                id="email"
              />
            </label>
            
          </div>
          <div
            className={
              navigate
                ? "opacity-100 flex flex-col gap-6"
                : "opacity-0 pointer-events-none hidden"
            }
          >
            {/* <label htmlFor="address">
            <div className="flex justify-between items-center">
                <span className="font-medium block">Address</span>
                {errors.address && (
                  <p className="text-red-500 text-sm">{errors.address.message}</p>
                )}
              </div>
              <input
                {...register("address", {
                  required: "This field is required",
                  maxLength: {
                    value: 500,
                    message: "Character limit exceeded",
                  },
                })}
                type="text"
                className="w-full h-[40px] border-2 border-solid border-gray-300 outline-none rounded-md p-4 md:text-base text-sm text-gray-700 mt-1"
                placeholder="Plot 6, Silicon Valley, USA"
                id="address"
              />
            </label> */}
            {/* <label htmlFor="agencyType">
            <div className="flex justify-between items-center">
                <span className="font-medium block">Agency Type</span>
                {errors.agency_type && (
                  <p className="text-red-500 text-sm">{errors.agency_type.message}</p>
                )}
              </div>
              <input
                {...register("agency_type", {required: "This field is required"})}
                type="text"
                className="w-full h-[40px] border-2 border-solid border-gray-300 outline-none rounded-md p-4 md:text-base text-sm text-gray-700 mt-1"
                placeholder="e.g Non-profit"
                id="agencyType"
              />
            </label> */}
            <label htmlFor="phone">
            <div className="flex justify-between items-center">
                <span className="font-medium block">Phone Number</span>
                {errors.phone_number && (
                  <p className="text-red-500 text-sm">{errors.phone_number.message}</p>
                )}
              </div>
              <input
                {...register("phone_number", {
                  required: "This is a required field",
                  minLength: {
                    value: 11,
                    message: "This field requires a minimum of 11 characters",
                  },
                  maxLength: {
                    value: 20,
                    message: "This field allows for a maximum of 20 characters",
                  },
                })}
                type="tel"
                className="w-full h-[40px] border-2 border-solid border-gray-300 outline-none rounded-md p-4 md:text-base text-sm text-gray-700 mt-1"
                placeholder="+123-456-789"
                id="phone"
              />
            </label>
            <label htmlFor="password">
            <div className="flex justify-between items-center">
                <span className="font-medium block">Password</span>
                {errors.password && (
                  <p className="text-red-500 text-sm">{errors.password.message}</p>
                )}
              </div>
              <input
                {...register("password", {
                  required: "Password is required",
                  minLength: {
                    value: 6,
                    message: "Minimum characters is 6",
                  },
                  pattern: {
                    value: /^(?=.*[A-Z]).+$/,
                    message:
                      "Uppercase character required",
                  },
                })}
                type="password"
                className="w-full h-[40px] border-2 border-solid border-gray-300 outline-none rounded-md p-4 md:text-base text-sm text-gray-700 mt-1"
                placeholder="Password"
                id="password"
              />
            </label>
          </div>
          <div
            id="buttons"
            className={
              navigate
                ? "flex justify-between items-center mt-10"
                : "flex justify-end items-center mt-10"
            }
          >
            <button
              type="button"
              className="h-10 w-24 bg-purple-500 rounded-md text-white"
              onClick={handleFormNavigation}
            >
              {navigate ? "Go back" : "Next Page"}
            </button>
            <input
              type="submit"
              value="Submit"
              className={
                navigate
                  ? "h-10 w-24 bg-purple-500 rounded-md text-white opacity-100"
                  : "opacity-0 hidden"
              }
            />
          </div>
        </form>
      </div>
    </div>
  );
}
