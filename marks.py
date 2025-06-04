#!/usr/bin/env python

def main():
    results = {
            "PRINCIPLES OF ELECTRICAL ENGINEERING": 96,
            "PROGRAMMING FOR ENGINEERS": 93.75,
            "ENGINEERING PRACTICE 1B": 87,
            "MATHEMATICAL MODELLING FOR ELECTRONICS AND ROBOTICS": 95,
            "COMPUTING PRACTICE": 98,
            "APPLIED ELECTRONICS": 86.81,
            "ENGINEERING PRACTICE 2": 85.25,
            "EMBEDDED SYSTEMS DESIGN": 89.5,
            "DIGITAL SYSTEM DESIGN": 89.5,
            "SYSTEMS ENGINEERING": 79.5,
            "SIGNALS AND SYSTEMS": 63.75,
            "ENGINEERING RESEARCH": 90.2,
            "GROUP DESIGN AND INTEGRATION PROJECT": 78.5,
            "POWER ELECTRONICS": 61.5,
            "EMBEDDED SYSTEMS DEVELOPMENT 1": 72.5,
            "PROFESSIONALISM FOR ENGINEERS": 74,
            "COMMUNICATIONS": 66,
            "CONTROL SYSTEMS DESIGN": 62.5,
            "FINAL YEAR PROJECT": 70  # placeholder
            }
    print(results.values())
    print(len(results))
    total = sum(results.values())
    print(f"Average = {total / len(results)}")

if __name__ == "__main__":
    main()
