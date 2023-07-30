package main

import (
  "encoding/json"
  "fmt"
  "io/ioutil"
  "net/http"
)

type CityTemp struct {
  Name        string `json:"name"`
  Temperature int    `json:"temperature"`
}

func apiGETTemp(city string, target interface{}) error {
  apiKey := "40b84815a1914e0fa68134954230407"
  url := fmt.Sprintf("http://api.weatherapi.com/v1/current.json?key=%s&q=%s", apiKey, city)

  response, err := http.Get(url)
  if err != nil {
    fmt.Println("Error:", err)
    return err
  }
  defer response.Body.Close()

  body, err := ioutil.ReadAll(response.Body)
  if err != nil {
    fmt.Println("Error:", err)
    return err
  }

  err = json.Unmarshal(body, &target)
  if err != nil {
    fmt.Println("Error:", err)
    return err
  }

  return nil
}

func main() {
  var repLon map[string]interface{}
  var repDel map[string]interface{}

  err := apiGETTemp("London", &repLon)
  if err != nil {
    fmt.Println("Error:", err)
    return
  }

  err = apiGETTemp("Delhi", &repDel)
  if err != nil {
    fmt.Println("Error:", err)
    return
  }

  cities := []CityTemp{
    {Name: "London", Temperature: int(repLon["current"].(map[string]interface{})["temp_c"].(float64))},
    {Name: "Delhi", Temperature: int(repDel["current"].(map[string]interface{})["temp_c"].(float64))},
  }

  fmt.Println(cities)

  for _, city := range cities {
    fmt.Println(city.Name)
    fmt.Println(city.Temperature)
  }
}
