from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import (
    noise_cancellation,
    silero,
    azure,
    google
)
from livekit.agents import mcp
from livekit.plugins.turn_detector.multilingual import MultilingualModel

load_dotenv(".env")

class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions="You are an arabic voice AI assistant.")

async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        stt=azure.STT(
            language="ar-SA"
        ),
        llm=google.LLM(
            model="gemini-2.0-flash-exp"
        ),
        tts=azure.TTS(
            voice="ar-SA-HamedNeural",
            language="ar-SA",
        ),
        vad=silero.VAD.load(),
        turn_detection=MultilingualModel(),
        mcp_servers=[mcp.MCPServerHTTP("http://127.0.0.1:8000/mcp/")]
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            # For telephony applications, use `BVCTelephony` instead for best results
            noise_cancellation=noise_cancellation.BVC(), 
        ),
    )

    await session.generate_reply(
        instructions="Greet the user and offer your assistance."
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))