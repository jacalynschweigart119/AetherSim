"""
Запуск бекенда AetherSim — REST API + планировщик симуляций.
"""
import uvicorn
from fastapi import FastAPI
from backend.routes import sim, agent, world
from backend.db.engine import init_db, close_db
from backend.scheduler.runner import SimulationRunner
from backend.logger import init_logger

app = FastAPI(title="AetherSim API", version="0.1.0")
init_logger(app)

# Роутеры
app.include_router(sim.router, prefix="/sim", tags=["Simulation"])
app.include_router(agent.router, prefix="/agent", tags=["Agent"])
app.include_router(world.router, prefix="/world", tags=["World"])

@app.on_event("startup")
async def on_startup():
    await init_db()
    app.state.runner = SimulationRunner()
    await app.state.runner.start_background()

@app.on_event("shutdown")
async def on_shutdown():
    await close_db()
    await app.state.runner.stop_background()

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
