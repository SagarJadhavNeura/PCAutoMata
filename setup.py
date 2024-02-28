from cx_Freeze import setup, Executable

setup(
    name="testSetup",
    version="1.0",
    description="Description of your app",
    executables=[Executable("start.py")],
)
