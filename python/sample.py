#Load data and parse date columnPython

import pandas as pd
import json
import json_maker
import numpy as np

class sample(object):
    def __init__(self):
        self.cli = json_maker.json_maker()

    def analyze(self, temp, stateName, countyName, cropName):
        acres_plant_str = cropName + " - ACRES PLANTED"
        acres_harv_str = cropName + " - ACRES HARVESTED"
        production_str = cropName + " - PRODUCTION, MEASURED IN BU"
        yield_str = cropName + " - YIELD, MEASURED IN BU / ACRE"
        sales_str = cropName + " - SALES, MEASURED IN $"
        
        acres_harvested = temp[ (temp.commodity == cropName) & (temp.state == stateName) & (temp.county == countyName) & (temp.data_item == acres_plant_str)]
        acres_planted = temp[ (temp.commodity == cropName) & (temp.state == stateName) & (temp.county == countyName) & (temp.data_item == acres_harv_str)]
        production = temp[ (temp.commodity == cropName) & (temp.state == stateName) & (temp.county == countyName) & (temp.data_item == production_str)]
        yield_measured = temp[ (temp.commodity == cropName) & (temp.state == stateName) & (temp.county == countyName) & (temp.data_item == yield_str)]
        sales = temp[ (temp.commodity == cropName) & (temp.state == stateName) & (temp.county == countyName) & (temp.data_item == sales_str)]
        
        acres_plant_irr_str = cropName + ", IRRIGATED - ACRES PLANTED"
        acres_harv_irr_str = cropName + ", IRRIGATED - ACRES HARVESTED"
        production_irr_str = cropName + ", IRRIGATED - PRODUCTION, MEASURED IN BU"
        yield_irr_str = cropName + ", IRRIGATED - YIELD, MEASURED IN BU / ACRE"
        acres_harvested_irr = temp[ (temp.commodity == cropName) & (temp.state == stateName) & (temp.county == countyName) & (temp.data_item == acres_plant_irr_str)]
        acres_planted_irr = temp[ (temp.commodity == cropName) & (temp.state == stateName) & (temp.county == countyName) & (temp.data_item == acres_harv_irr_str)]
        production_irr = temp[ (temp.commodity == cropName) & (temp.state == stateName) & (temp.county == countyName) & (temp.data_item == production_irr_str)]
        yield_measured_irr = temp[ (temp.commodity == cropName) & (temp.state == stateName) & (temp.county == countyName) & (temp.data_item == yield_irr_str)]
         
        acres_plant_nirr_str = cropName + ", NON-IRRIGATED - ACRES PLANTED"
        acres_harv_nirr_str = cropName + ", NON-IRRIGATED - ACRES HARVESTED"
        production_nirr_str = cropName + ", NON-IRRIGATED - PRODUCTION, MEASURED IN BU"
        yield_nirr_str = cropName + ", NON-IRRIGATED - YIELD, MEASURED IN BU / ACRE"
        acres_harvested_nirr = temp[ (temp.commodity == cropName) & (temp.state == stateName) & (temp.county == countyName) & (temp.data_item == acres_plant_nirr_str)]
        acres_planted_nirr = temp[ (temp.commodity == cropName) & (temp.state == stateName) & (temp.county == countyName) & (temp.data_item == acres_harv_nirr_str)]
        production_nirr = temp[ (temp.commodity == cropName) & (temp.state == stateName) & (temp.county == countyName) & (temp.data_item == production_nirr_str)]
        yield_measured_nirr = temp[ (temp.commodity == cropName) & (temp.state == stateName) & (temp.county == countyName) & (temp.data_item == yield_nirr_str)]
        list = {}
        
        list.update({'acres_harvested': acres_harvested.value.mean().round(2)})
        list.update({'acres_planted': acres_planted.value.mean().round(2)})
        list.update({'production': production.value.mean().round(2)})
        list.update({'yield': yield_measured.value.mean().round(2)})
        list.update({'sales': sales.value.mean().round(2)})
        list.update({'acres_harvested_irr': acres_harvested_irr.value.mean().round(2)})
        list.update({'acres_planted_irr': acres_planted_irr.value.mean().round(2)})
        list.update({'production_irr': production_irr.value.mean().round(2)})
        list.update({'yield_irr': yield_measured_irr.value.mean().round(2)})
        list.update({'acres_harvested_nirr': acres_harvested_nirr.value.mean().round(2)})
        list.update({'acres_planted_nirr': acres_planted_nirr.value.mean().round(2)})
        list.update({'production_nirr': production_nirr.value.mean().round(2)})
        list.update({'yield_nirr': yield_measured_nirr.value.mean().round(2)})

        a = self.cli.prepare(list, cropName)
        return a