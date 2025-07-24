"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
},
    # Music activities
    "Music Band": {
        "description": "Join the school band and perform at events",
        "schedule": "Mondays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 10,
        "participants": ["amelia@mergington.edu", "ethan@mergington.edu"]
    },
    # Science activities
    "Robotics Club": {
        "description": "Build and program robots for competitions",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["harper@mergington.edu", "jackson@mergington.edu"]
    }
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    # Sports activities
    "Soccer Team": {
        "description": "Join the school soccer team and compete in local leagues",
        "schedule": "Wednesdays and Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 18,
        "participants": ["lucas@mergington.edu", "mia@mergington.edu"]
    },
    "Basketball Club": {
        "description": "Practice basketball skills and play friendly matches",
        "schedule": "Tuesdays, 5:00 PM - 6:30 PM",
        "max_participants": 15,
        "participants": ["liam@mergington.edu", "ava@mergington.edu"]
    },
    # Artistic activities
    "Art Club": {
        "description": "Explore painting, drawing, and other visual arts",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 16,
        "participants": ["noah@mergington.edu", "isabella@mergington.edu"]
    },
    },
        # Additional activities
        "Drama Club": {
            "description": "Participate in plays and improve acting skills",
            "schedule": "Tuesdays and Fridays, 4:00 PM - 5:30 PM",
            "max_participants": 20,
            "participants": ["charlotte@mergington.edu", "henry@mergington.edu"]
        },
        "Photography Club": {
            "description": "Learn photography techniques and work on creative projects",
            "schedule": "Wednesdays, 3:00 PM - 4:30 PM",
            "max_participants": 15,
            "participants": ["ella@mergington.edu", "james@mergington.edu"]
        }
    }
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Already signed up for this activity")
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}

@app.delete("/activities/{activity_name}")
def delete_activity(activity_name: str):
    """Delete an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Remove the activity
    del activities[activity_name]
    return {"message": f"Activity '{activity_name}' has been deleted"}