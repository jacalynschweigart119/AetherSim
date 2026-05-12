



















































from fastapi import APIRouter, Depends
from backend.db.models import Simulation, get_session
from backend.scheduler.runner import SimulationRunner

router = APIRouter()

@router.post("/start")
async def start_simulation(name: str, runner: SimulationRunner = Depends(SimulationRunner.get_instance)):
    sim_id = await runner.start_new_simulation(name)
    return {"status": "started", "simulation_id": sim_id}

@router.get("/status/{sim_id}")
async def get_simulation_status(sim_id: str, runner: SimulationRunner = Depends(SimulationRunner.get_instance)):
    return await runner.get_status(sim_id)

@router.post("/stop/{sim_id}")
async def stop_simulation(sim_id: str, runner: SimulationRunner = Depends(SimulationRunner.get_instance)):
    await runner.stop_simulation(sim_id)
    return {"status": "stopped", "simulation_id": sim_id}
