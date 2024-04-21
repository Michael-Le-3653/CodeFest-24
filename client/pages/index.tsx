import Example from "@/components/Example";
import ChatBubble from "@/components/ChatBubble";
import InputField from "@/components/InputField";
import Header from "@/components/Header";
export default function Home() {
  return (
    <>
      <Header/>
      <div className="bg-black flex flex-col h-screen px-10 py-5">
                      
        <ChatBubble/>
        <div className="chat-input-field">
          <InputField/>
        </div>
  </div>
    </>
  )
}
