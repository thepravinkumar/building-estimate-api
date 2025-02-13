# Building Estimate API

This API calculates the approximate construction cost of a building based on the latest CPWD estimates.

## **How to Use**
- Send a `POST` request to `/estimate` with JSON body:
  ```json
  {
    "baseArea": 100,
    "floorHeight": 3,
    "totalFloors": 5
  }
{
  "estimatedCost": 37500000
}
