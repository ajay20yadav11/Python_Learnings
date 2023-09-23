package main

import (
  "encoding/json"
  "fmt"
  "net/http"
  "io/ioutil"
)


type CityTemp struct {
  Name        string
  Temperature map[string]interface{}
}


func apiGETTemp(city string) map[string]interface{} {

  apiKey := "40b84815a1914e0fa68134954230407"
  // city := "Mumbai"
  url := fmt.Sprintf("http://api.weatherapi.com/v1/current.json?key=%s&q=%s", apiKey, city)

  // this will send an API request and is using net/http package
  response, err := http.Get(url)

  // incase if there is an error while doing GET API request
  if err != nil {
    fmt.Println("Error:", err)
    return nil
  }

  // This is to say that don"t close immediately but close this at later stage or close if before a return statement
  defer response.Body.Close()

  // Read the response body
  body, err := ioutil.ReadAll(response.Body)
  if err != nil {
    fmt.Println("Error:", err)
    return nil
  }

  // Print the response body
  var data map[string]interface{}
  fmt.Println("**********************************************************************************************************")
  fmt.Printf("%s", body)


  fmt.Println(data)
  if err := json.Unmarshal(body, &data); err != nil {
    fmt.Println("Error: ", err)
    return nil
  }
  fmt.Println("**********************************************************************************************************")
  fmt.Println(data)

  return data
}


func main() {

  cities := []CityTemp{}
  allCities := []string{}
  for {
    fmt.Print("Please enter a city name (or 'Quit' to exit): ")
    var getCityName string
    fmt.Scanln(&getCityName)
    if getCityName == "Quit" || getCityName == "QUIT" || getCityName == "quit" || getCityName == "q" || getCityName == "Q" {
      break
    }
    allCities = append(allCities, getCityName)
  } 

  for _, anim := range allCities {
    cityData := CityTemp{Name: anim, Temperature: apiGETTemp(anim)}
    cities = append(cities, cityData)
  }

  for _, anim := range cities {
    locationName := anim.Name
    tempValue := anim.Temperature["current"].(map[string]interface{})["temp_c"]
    fmt.Printf("The Temperature in %v is %v as per Celcius convention ", locationName, tempValue)
    fmt.Println()
  }
}