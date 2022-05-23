import sys
import datetime
import math
from numpy import mat, result_type
from numpy.lib.histograms import _hist_bin_auto
import pandas as pd
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

class ModelCrossingAssessmentCA(qtc.QObject):
    
    def __init__(self, view):
        super().__init__()
        self.view = view
        
    #Calculate collision_history_total_5_year_period
    def collision_history_total_5_year_period(self):       
        collision_history_fatal_injury = self.view.spinBox_collision_history_fatal_injury.value()
        collision_history_personal_injury = self.view.spinBox_collision_history_personal_injury.value()
        collision_history_property_damage = self.view.spinBox_collision_history_property_damage.value()
        
        result = sum([collision_history_fatal_injury, collision_history_personal_injury, collision_history_property_damage])
        self.view.label_collision_history_total_5_year_period.setNum(result)
        return result
    

    #Calculate collision_history_risk_index_initial
    def collision_history_risk_index_initial(self):
        general_info_rail_no_tracks_total = self.general_info_rail_no_tracks_total()
        inspection_details_gcws_type = self.view.comboBox_inspection_details_gcws_type.currentText()
        gcws_observe_gates_n_or_e_approach = self.view.comboBox_gcws_observe_gates_n_or_e_approach.currentText()
        gcws_observe_gates_s_or_w_approach = self.view.comboBox_gcws_observe_gates_s_or_w_approach.currentText()

        grade_crossing_surface_observe_road_approach_surface_type = self.view.comboBox_grade_crossing_surface_observe_road_approach_surface_type.currentText()
        general_info_road_classification = self.view.comboBox_general_info_road_classification.currentText()
 
        c = self.view.spinBox_general_info_road_aadt_current.value()               # c = annual average number of highway vehicles per day (total both directions)
        t = self.general_info_rail_no_trains_per_day_total() # t = average total train movements per day
        d = self.general_info_rail_no_trains_per_day_total() # d = average number of thru trains per day during daylight
        mt = self.view.spinBox_general_info_rail_no_tracks_main.value()             # mt = number of main tracks
        ms = self.general_info_rail_railway_design_speed()   # ms = maximum timetable speed, mph
        hl = self.general_info_road_no_traffic_lanes_total() # hl = number of highway lanes
        
        # hp = highway paved, yes = 1.0, no = 2.0
        split_general_info_road_classification = general_info_road_classification.split()

        if not split_general_info_road_classification:
            hp = 'No Value'
        elif split_general_info_road_classification[1] == 'Freeway' and grade_crossing_surface_observe_road_approach_surface_type == 'Asphalt':
            hp = 1.0
        else:
            hp = 2.0

        #ht = highway type factor value
        dict_general_info_road_classification = dict([
            ('Rural Local Undivided', 4),
            ('Rural Collector Undivided', 3),
            ('Rural Collector Divided', 3),
            ('Rural Arterial Undivided', 2),
            ('Rural Arterial Divided', 2),
            ('Rural Freeway Divided', 1),
            ('Urban Local Undivided', 4),
            ('Urban Collector Undivided', 3),
            ('Urban Collector Divided', 3),
            ('Urban Arterial Undivided', 2),
            ('Urban Arterial Divided', 2),
            ('Private Road', 5),
            ('Pedestrian Crossing', 5)
            ])
        if general_info_road_classification == '':
            ht = 'No Value'
        else:
            ht = dict_general_info_road_classification[general_info_road_classification]       

        if inspection_details_gcws_type == '' or general_info_road_classification == '' or grade_crossing_surface_observe_road_approach_surface_type == '' or gcws_observe_gates_n_or_e_approach == '' or gcws_observe_gates_s_or_w_approach == '' or general_info_rail_no_tracks_total == 'No Value' or mt == 'No Value' or c == 0 or t == 'No Value' or d == 'No Value' or ms == 'No Value' or hl == 'No Value' or hp == 'No Value' or ht == 'No Value':            
            result = "No Value"
            self.view.label_collision_history_risk_index_initial.setText(result)
        elif inspection_details_gcws_type == 'Passive':
            result = round(0.002268 * math.pow(((c * t + 0.2)/0.2), 0.3334) * math.exp(0.2094 * mt) * math.pow(((d + 0.2)/0.2), 0.1336) * math.exp(-0.616 * (hp - 1)) * math.exp(0.0077 * ms) * math.exp(-0.1000 * (ht - 1)) * 1, 5)
            self.view.label_collision_history_risk_index_initial.setNum(result)
        elif inspection_details_gcws_type == 'Active' and (gcws_observe_gates_n_or_e_approach != 'Yes' or gcws_observe_gates_s_or_w_approach != 'Yes') and (gcws_observe_gates_n_or_e_approach != '' or gcws_observe_gates_s_or_w_approach != ''):
            result = round(0.003646 * math.pow(((c * t + 0.2)/0.2), 0.2953) * math.exp(0.1088 * mt) * math.pow(((d + 0.2)/0.2), 0.047) * 1 * 1 * 1 * math.exp(0.1380 * (hl - 1)), 5)
            self.view.label_collision_history_risk_index_initial.setNum(result)
        elif inspection_details_gcws_type == 'Active' and (gcws_observe_gates_n_or_e_approach == 'Yes' or gcws_observe_gates_s_or_w_approach == 'Yes'):
            result = round(0.001088 * math.pow(((c * t + 0.2)/0.2), 0.3116) * math.exp(0.2912 * mt) * 1 * 1 * 1 * 1 * math.exp(0.1036 * (hl - 1)) ,5)
            self.view.label_collision_history_risk_index_initial.setNum(result)
        else:
            result = 'No Value'
            self.view.label_collision_history_risk_index_initial.setText(result)
        return result
    
    #Calculate collision_history_risk_index_final
    def collision_history_risk_index_final(self):
        collision_history_risk_index_initial = self.collision_history_risk_index_initial()
        collision_history_total_5_year_period = self.collision_history_total_5_year_period()

        if collision_history_risk_index_initial == 'No Value':
            result = 'No Value'
            self.view.label_collision_history_risk_index_final.setText(result)
        else:
            result = round(
                sum([ 
                (1/sum([0.05,collision_history_risk_index_initial])) * collision_history_risk_index_initial / sum([5, 1 / sum([0.05, collision_history_risk_index_initial])]),
                collision_history_total_5_year_period / sum([5, 1 / sum([0.05, collision_history_risk_index_initial])])
                ]),
                5)
            self.view.label_collision_history_risk_index_final.setNum(result)
        return result

    #Calculate general_info_rail_no_tracks_total
    def general_info_rail_no_tracks_total(self):      
        general_info_rail_no_tracks_main = self.view.spinBox_general_info_rail_no_tracks_main.value()
        general_info_rail_no_tracks_other = self.view.spinBox_general_info_rail_no_tracks_other.value()
        
        if general_info_rail_no_tracks_main == 0 and general_info_rail_no_tracks_other == 0:
            result = 'No Value'
            self.view.label_general_info_rail_no_tracks_total.setText(result)
        else:
            result = sum([general_info_rail_no_tracks_main, general_info_rail_no_tracks_other])
            self.view.label_general_info_rail_no_tracks_total.setNum(result)
        return result

    #Calculate general_info_rail_no_trains_per_day_total
    def general_info_rail_no_trains_per_day_total(self):       
        general_info_rail_no_trains_per_day_freight = self.view.spinBox_general_info_rail_no_trains_per_day_freight.value()
        general_info_rail_no_trains_per_day_passengers = self.view.spinBox_general_info_rail_no_trains_per_day_passengers.value()
        
        if general_info_rail_no_trains_per_day_freight == 0 and general_info_rail_no_trains_per_day_passengers == 0:
            result = 'No Value'
            self.view.label_general_info_rail_no_trains_per_day_total.setText(result)    
        else:
            result = sum([general_info_rail_no_trains_per_day_freight, general_info_rail_no_trains_per_day_passengers])
            self.view.label_general_info_rail_no_trains_per_day_total.setNum(result)
        return result

    #Calculate general_info_road_no_traffic_lanes_total
    def general_info_road_no_traffic_lanes_total(self):     
        general_info_road_no_traffic_lanes_bidirectional = self.view.spinBox_general_info_road_no_traffic_lanes_bidirectional.value()
        general_info_road_no_traffic_lanes_northbound_or_eastbound = self.view.spinBox_general_info_road_no_traffic_lanes_northbound_or_eastbound.value()
        general_info_road_no_traffic_lanes_southbound_or_westbound = self.view.spinBox_general_info_road_no_traffic_lanes_southbound_or_westbound.value()        
        
        if general_info_road_no_traffic_lanes_bidirectional == 0 and general_info_road_no_traffic_lanes_northbound_or_eastbound == 0 and general_info_road_no_traffic_lanes_southbound_or_westbound == 0:
            result = 'No Value'
            self.view.label_general_info_road_no_traffic_lanes_total.setText(result)
        else:
            result = sum([general_info_road_no_traffic_lanes_bidirectional, general_info_road_no_traffic_lanes_northbound_or_eastbound, general_info_road_no_traffic_lanes_southbound_or_westbound])
            self.view.label_general_info_road_no_traffic_lanes_total.setNum(result)
        return result

    #Calculate general_info_rail_railway_design_speed
    def general_info_rail_railway_design_speed(self):
        general_info_rail_max_railway_operating_speed_freight = self.view.spinBox_general_info_rail_max_railway_operating_speed_freight.value()
        general_info_rail_max_railway_operating_speed_passenger = self.view.spinBox_general_info_rail_max_railway_operating_speed_passenger.value()        
        
        if general_info_rail_max_railway_operating_speed_freight == 0 and general_info_rail_max_railway_operating_speed_passenger == 0:
            result = 'No Value'
            self.view.label_general_info_rail_railway_design_speed.setText(result)
        else:
            result = max((general_info_rail_max_railway_operating_speed_freight, general_info_rail_max_railway_operating_speed_passenger))
            self.view.label_general_info_rail_railway_design_speed.setNum(result)
        return result

    # DESIGN CONSIDERATIONS (GCS SECTION 10)
    #Calculate design_calculate_adjacent_track_clearance_time
    def design_calculate_adjacent_track_clearance_time(self):        
        design_measure_adjacent_track_separation_distance = self.view.doubleSpinBox_design_measure_adjacent_track_separation_distance.value()
        design_measure_adjacent_track_clearance_distance = self.view.doubleSpinBox_design_measure_adjacent_track_clearance_distance.value()

        if design_measure_adjacent_track_separation_distance<30.0 or design_measure_adjacent_track_separation_distance>60.0:
            result = "N/A"
            self.view.label_design_calculate_adjacent_track_clearance_time.setText(result)
        elif design_measure_adjacent_track_separation_distance>=30.0 and design_measure_adjacent_track_separation_distance<=60.0:
            result = math.ceil(sum([20.00,max(0.00,design_measure_adjacent_track_clearance_distance-10.668)/3.048]))
            self.view.label_design_calculate_adjacent_track_clearance_time.setNum(result)
        return result

    #Calculate design_calculate_clearance_time_pedestrian_design_check
    def design_calculate_clearance_time_pedestrian_design_check(self):
        design_measure_clearance_distance_pedestrian = self.view.doubleSpinBox_design_measure_clearance_distance_pedestrian.value()
        
        result = math.ceil(design_measure_clearance_distance_pedestrian/1.22)
        self.view.label_design_calculate_clearance_time_pedestrian_design_check.setNum(result)
        return result

    #Calculate design_calculate_clearance_time_vehicle_design_check
    def design_calculate_clearance_time_vehicle_design_check(self):
        design_input_reaction_time = self.view.label_design_input_reaction_time.text()
        design_calculate_vehicle_departure_time_grade_adjusted = self.design_calculate_vehicle_departure_time_grade_adjusted()
        
        if design_calculate_vehicle_departure_time_grade_adjusted == 'N/A':
            result = 'N/A'
            self.view.label_design_calculate_clearance_time_vehicle_design_check.setText(result)
        elif design_calculate_vehicle_departure_time_grade_adjusted == 'No Value':
            result = 'No Value'
            self.view.label_design_calculate_clearance_time_vehicle_design_check.setText(result)
        else:
            design_input_reaction_time = float(design_input_reaction_time)
            design_calculate_vehicle_departure_time_crossing_grade_adjusted = float(design_calculate_vehicle_departure_time_grade_adjusted)
            result = math.ceil(sum([design_input_reaction_time,design_calculate_vehicle_departure_time_crossing_grade_adjusted]))
            self.view.label_design_calculate_clearance_time_vehicle_design_check.setNum(result)
        return result

    #TODO
    #Calculate design_calculate_gate_arm_clearance_time_pedestrian
    def design_calculate_gate_arm_clearance_time_pedestrian(self):
        pass

    #Calculate design_calculate_gate_arm_clearance_time_vehicle_ssd
    def design_calculate_gate_arm_clearance_time_vehicle_ssd(self):
        general_info_road_speed_design = self.view.spinBox_general_info_road_speed_design.value()
        design_road_design_vehicle_type = self.view.comboBox_design_road_design_vehicle_type.currentText()
        design_lookup_design_vehicle_length = self.design_lookup_design_vehicle_length()
        sightlines_lookup_ssd_minimum_n_or_e_approach = self.sightlines_lookup_ssd_minimum_n_or_e_approach()
        sightlines_lookup_ssd_minimum_s_or_w_approach = self.sightlines_lookup_ssd_minimum_s_or_w_approach()

        if design_road_design_vehicle_type == "Pedestrian Only":
            result = "N/A"
            self.view.label_design_calculate_gate_arm_clearance_time_vehicle_ssd.setText(result)
        elif design_road_design_vehicle_type == '' or design_lookup_design_vehicle_length == "No Value" or sightlines_lookup_ssd_minimum_n_or_e_approach == "No Value" or sightlines_lookup_ssd_minimum_s_or_w_approach == "No Value" or general_info_road_speed_design == 0:
            result = "No Value"
            self.view.label_design_calculate_gate_arm_clearance_time_vehicle_ssd.setText(result)
        else:
            design_lookup_design_vehicle_length = float(design_lookup_design_vehicle_length)
            sightlines_lookup_ssd_minimum_n_or_e_approach = float(sightlines_lookup_ssd_minimum_n_or_e_approach)
            sightlines_lookup_ssd_minimum_s_or_w_approach = float(sightlines_lookup_ssd_minimum_s_or_w_approach)
            result = math.ceil(sum([max(sightlines_lookup_ssd_minimum_n_or_e_approach, sightlines_lookup_ssd_minimum_s_or_w_approach), 2.0, design_lookup_design_vehicle_length]) / (0.278 * general_info_road_speed_design))
            self.view.label_design_calculate_gate_arm_clearance_time_vehicle_ssd.setNum(result)
        return result

    #Calculate design_calculate_gate_arm_clearance_time_vehicle_stop
    def design_calculate_gate_arm_clearance_time_vehicle_stop(self):
        design_input_reaction_time = self.view.label_design_input_reaction_time.text()
        design_lookup_grade_adjustment_factor = self.design_lookup_grade_adjustment_factor()
        design_calculate_vehicle_departure_time_gate_arm_clearance = self.design_calculate_vehicle_departure_time_gate_arm_clearance()

        if design_calculate_vehicle_departure_time_gate_arm_clearance == 'N/A' or design_lookup_grade_adjustment_factor == 'N/A':
            result = 'N/A'
            self.view.label_design_calculate_gate_arm_clearance_time_vehicle_stop.setText(result)
        elif design_calculate_vehicle_departure_time_gate_arm_clearance == 'No Value' or design_lookup_grade_adjustment_factor == 'No Value':
            result = 'No Value'
            self.view.label_design_calculate_gate_arm_clearance_time_vehicle_stop.setText(result)
        else:
            design_input_reaction_time = float(design_input_reaction_time)
            design_calculate_vehicle_departure_time_gate_arm_clearance = float(design_calculate_vehicle_departure_time_gate_arm_clearance)
            design_lookup_grade_adjustment_factor = float(design_lookup_grade_adjustment_factor)
            result = math.ceil(sum([design_input_reaction_time, design_calculate_vehicle_departure_time_gate_arm_clearance * design_lookup_grade_adjustment_factor]))
            self.view.label_design_calculate_gate_arm_clearance_time_vehicle_stop.setNum(result)
        return result

    #Calculate design_calculate_gate_arm_clearance_time_vehicle_recommended
    def design_calculate_gate_arm_clearance_time_vehicle_recommended(self):
        design_calculate_gate_arm_clearance_time_vehicle_ssd = self.design_calculate_gate_arm_clearance_time_vehicle_ssd()
        design_calculate_gate_arm_clearance_time_vehicle_stop = self.design_calculate_gate_arm_clearance_time_vehicle_stop()

        if design_calculate_gate_arm_clearance_time_vehicle_ssd == 'N/A' or design_calculate_gate_arm_clearance_time_vehicle_stop == 'N/A':
            result = 'N/A'
            self.view.label_design_calculate_gate_arm_clearance_time_vehicle_recommended.setText(result)
        elif design_calculate_gate_arm_clearance_time_vehicle_ssd == 'No Value' or design_calculate_gate_arm_clearance_time_vehicle_ssd == 'No Value':
            result = 'No Value'
            self.view.label_design_calculate_gate_arm_clearance_time_vehicle_recommended.setText(result)
        else:
            design_calculate_clearance_time_gate_arm_ssd = int(design_calculate_gate_arm_clearance_time_vehicle_ssd)
            design_calculate_clearance_time_gate_arm_stop = int(design_calculate_gate_arm_clearance_time_vehicle_ssd)
            result = max(design_calculate_clearance_time_gate_arm_ssd, design_calculate_clearance_time_gate_arm_stop)
            self.view.label_design_calculate_gate_arm_clearance_time_vehicle_recommended.setNum(result)
        return result

    #Calulcate design_calculate_vehicle_departure_time
    def design_calculate_vehicle_departure_time(self):
        design_measure_clearance_distance_pedestrian = self.view.doubleSpinBox_design_measure_clearance_distance_pedestrian.value()
        design_calculate_vehicle_travel_distance = self.design_calculate_vehicle_travel_distance()
        design_lookup_design_vehicle_class = self.design_lookup_design_vehicle_class()
        
        if design_lookup_design_vehicle_class == 'Pedestrian':
            result = 'N/A'
            self.view.label_design_calculate_vehicle_departure_time.setText(result)
        elif design_lookup_design_vehicle_class == 'No Value' or design_calculate_vehicle_travel_distance == 'No Value':
            result = 'No Value'
            self.view.label_design_calculate_vehicle_departure_time.setText(result)
        elif design_lookup_design_vehicle_class == 'Cars' and design_calculate_vehicle_travel_distance != 'No Value':
            design_calculate_vehicle_travel_distance = float(design_calculate_vehicle_travel_distance)
            result = round(max(4.00,-1.83359063314625E-07 * math.pow(design_calculate_vehicle_travel_distance, 4) + 0.000030862217902978 * math.pow(design_calculate_vehicle_travel_distance, 3) - 0.00243559236227734 * math.pow(design_calculate_vehicle_travel_distance, 2) + 0.194096256511465 * design_calculate_vehicle_travel_distance + 1.9653478726958),4)
            self.view.label_design_calculate_vehicle_departure_time.setNum(result)
        elif design_lookup_design_vehicle_class == 'Single-Unit Trucks' and design_calculate_vehicle_travel_distance != 'No Value':
            design_calculate_vehicle_travel_distance = float(design_calculate_vehicle_travel_distance)
            result = round(max(6.00,2.95895110935529E-06 * math.pow(design_calculate_vehicle_travel_distance, 3) - 0.00120538991988588 * math.pow(design_calculate_vehicle_travel_distance, 2) + 0.23080739982193 * design_calculate_vehicle_travel_distance + 3.11489082547138),4)
            self.view.label_design_calculate_vehicle_departure_time.setNum(result)
        elif (design_lookup_design_vehicle_class == 'Tractor Trailers' or design_lookup_design_vehicle_class == 'Combination Vehicles' or design_lookup_design_vehicle_class == 'Buses') and design_calculate_vehicle_travel_distance != 'No Value':
            design_calculate_vehicle_travel_distance = float(design_calculate_vehicle_travel_distance)
            result = round(max(7.00,2.43585710133203E-07 * math.pow(design_calculate_vehicle_travel_distance, 4) - 0.0000473118786681759 * math.pow(design_calculate_vehicle_travel_distance, 3) + 0.00169819852156627 * math.pow(design_calculate_vehicle_travel_distance, 2) + 0.211550565362998 * design_calculate_vehicle_travel_distance + 3.96662867415871),4)
            self.view.label_design_calculate_vehicle_departure_time.setNum(result)        
        elif design_lookup_design_vehicle_class == 'Pedestrian' and design_calculate_vehicle_travel_distance != 'No Value':
            result = round(design_measure_clearance_distance_pedestrian/1.22,4)
            self.view.label_design_calculate_vehicle_departure_time.setNum(result)
        return result

    #Calculate design_calculate_vehicle_departure_time_grade_adjusted
    def design_calculate_vehicle_departure_time_grade_adjusted(self):
        design_calculate_vehicle_departure_time = self.design_calculate_vehicle_departure_time()
        design_lookup_grade_adjustment_factor = self.design_lookup_grade_adjustment_factor()

        if design_calculate_vehicle_departure_time == 'N/A':
            result = 'N/A'
            self.view.label_design_calculate_vehicle_departure_time_grade_adjusted.setText(result)
        elif design_calculate_vehicle_departure_time == 'No Value' or design_lookup_grade_adjustment_factor == 'No Value':
            result = 'No Value'
            self.view.label_design_calculate_vehicle_departure_time_grade_adjusted.setText(result)
        else:
            design_lookup_vehicle_departure_time = float(design_calculate_vehicle_departure_time)
            design_lookup_grade_adjustment_factor = float(design_lookup_grade_adjustment_factor)
            result = design_lookup_vehicle_departure_time * design_lookup_grade_adjustment_factor
            self.view.label_design_calculate_vehicle_departure_time_grade_adjusted.setNum(result)
        return result

    #Calculate design_calculate_vehicle_departure_time_gate_arm_clearance
    def design_calculate_vehicle_departure_time_gate_arm_clearance(self):
        design_lookup_design_vehicle_class = self.design_lookup_design_vehicle_class()
        design_lookup_design_vehicle_length = self.design_lookup_design_vehicle_length()

        if design_lookup_design_vehicle_class == 'Pedestrian':
            result = 'N/A'
            self.view.label_design_calculate_vehicle_departure_time_gate_arm_clearance.setText(result)
        elif design_lookup_design_vehicle_class == 'No Value' or design_lookup_design_vehicle_length == 'No Value':
            result = 'No Value'
            self.view.label_design_calculate_vehicle_departure_time_gate_arm_clearance.setText(result)
        elif design_lookup_design_vehicle_class == 'Cars' and design_lookup_design_vehicle_length != 'No Value':
            design_lookup_design_vehicle_length = float(design_lookup_design_vehicle_length)
            result = round(max(4.00,-1.83359063314625E-07 * math.pow(sum([design_lookup_design_vehicle_length,2.00]), 4) + 0.000030862217902978 * math.pow(sum([design_lookup_design_vehicle_length,2.00]), 3) - 0.00243559236227073 * math.pow(sum([design_lookup_design_vehicle_length,2.00]), 2) + 0.194096256511465 * sum([design_lookup_design_vehicle_length,2.00]) + 1.9653478726958),4)
            self.view.label_design_calculate_vehicle_departure_time_gate_arm_clearance.setNum(result)
        elif design_lookup_design_vehicle_class == 'Single-Unit Trucks' and design_lookup_design_vehicle_length != 'No Value':            
            design_lookup_design_vehicle_length = float(design_lookup_design_vehicle_length)
            result = round(max(6.00,2.95895110935529E-06 * math.pow(sum([design_lookup_design_vehicle_length,2.00]), 3) - 0.00120538991988588 * math.pow(sum([design_lookup_design_vehicle_length,2.00]), 2) + 0.23080739982193 * sum([design_lookup_design_vehicle_length,2.00]) + 3.11489082547138),4)
            self.view.label_design_calculate_vehicle_departure_time_gate_arm_clearance.setNum(result)
        elif (design_lookup_design_vehicle_class == 'Tractor Trailers' or design_lookup_design_vehicle_class == 'Combination Vehicles' or design_lookup_design_vehicle_class == 'Buses') and design_lookup_design_vehicle_length != 'No Value':
            design_lookup_design_vehicle_length = float(design_lookup_design_vehicle_length)
            result = round(max(7.00,2.43585710133203E-07 * math.pow(sum([design_lookup_design_vehicle_length,2.00]), 4) - 0.0000473118786681759 * math.pow(sum([design_lookup_design_vehicle_length,2.00]), 3) + 0.00169819852156627 * math.pow(sum([design_lookup_design_vehicle_length,2.00]), 2) + 0.211550565362998 * sum([design_lookup_design_vehicle_length,2.00]) + 3.96662867415871),4)
            self.view.label_design_calculate_vehicle_departure_time_gate_arm_clearance.setNum(result)
        return result

    #Calculate design_calculate_vehicle_departure_time_gate_arm_clearance_grade_adjusted
    def design_calculate_vehicle_departure_time_gate_arm_clearance_grade_adjusted(self):
        design_calculate_vehicle_departure_time_gate_arm_clearance = self.design_calculate_vehicle_departure_time_gate_arm_clearance()
        design_lookup_grade_adjustment_factor = self.design_lookup_grade_adjustment_factor()

        if design_calculate_vehicle_departure_time_gate_arm_clearance == 'N/A':
            result = 'N/A'
            self.view.label_design_calculate_vehicle_departure_time_grade_adjusted.setText(result)
        elif design_calculate_vehicle_departure_time_gate_arm_clearance == 'No Value' or design_lookup_grade_adjustment_factor == 'No Value':
            result = 'No Value'
            self.view.label_design_calculate_vehicle_departure_time_grade_adjusted.setText(result)
        else:
            design_calculate_vehicle_departure_time_gate_arm_clearance = float(design_calculate_vehicle_departure_time_gate_arm_clearance)
            design_lookup_grade_adjustment_factor = float(design_lookup_grade_adjustment_factor)
            result = design_calculate_vehicle_departure_time_gate_arm_clearance * design_lookup_grade_adjustment_factor
            self.view.label_design_calculate_vehicle_departure_time_grade_adjusted.setNum(result)
        return result

    #Calculate design_calculate_vehicle_travel_distance
    def design_calculate_vehicle_travel_distance(self):
        design_measure_clearance_distance_vehicle = self.view.doubleSpinBox_design_measure_clearance_distance_vehicle.value()
        design_road_design_vehicle_type = self.view.comboBox_design_road_design_vehicle_type.currentText()
        design_lookup_design_vehicle_length = self.design_lookup_design_vehicle_length()

        if design_road_design_vehicle_type == 'Pedestrian Only':
            result = 'N/A'
            self.view.label_design_calculate_vehicle_travel_distance.setText(result)
        elif design_measure_clearance_distance_vehicle == 0.00 or design_lookup_design_vehicle_length == 'No Value':
            result = 'No Value'
            self.view.label_design_calculate_vehicle_travel_distance.setText(result)
        else:
            design_lookup_design_vehicle_length = float(design_lookup_design_vehicle_length)          
            result = sum([design_measure_clearance_distance_vehicle, design_lookup_design_vehicle_length])
            self.view.label_design_calculate_vehicle_travel_distance.setNum(result)
        return result

    #Calculate design_lookup_design_vehicle_class
    def design_lookup_design_vehicle_class(self):
        design_road_design_vehicle_type = self.view.comboBox_design_road_design_vehicle_type.currentText()
        df_table_4_1_general_vehicles = pd.read_csv(r'resources\\railway_data\\track_and_roadway\\custom\\table_4_1_general_vehicles.csv')

        if design_road_design_vehicle_type == '':
            result = 'No Value'
            self.view.label_design_lookup_design_vehicle_class.setText(result)
        else:
            result = df_table_4_1_general_vehicles.loc[df_table_4_1_general_vehicles.general_vehicle_descriptions == f'{design_road_design_vehicle_type}','class'].item()
            self.view.label_design_lookup_design_vehicle_class.setText(result)
        return result

    #Calculate design_lookup_design_vehicle_length
    def design_lookup_design_vehicle_length(self):
        design_road_design_vehicle_type = self.view.comboBox_design_road_design_vehicle_type.currentText()
        df_table_4_1_general_vehicles = pd.read_csv(r'resources\\railway_data\\track_and_roadway\\custom\\table_4_1_general_vehicles.csv')
        
        if design_road_design_vehicle_type == '':
            result = 'No Value'
            self.view.label_design_lookup_design_vehicle_length.setText(result)
        elif design_road_design_vehicle_type == 'Pedestrian Only':
            result = 0.0
            self.view.label_design_lookup_design_vehicle_length.setNum(result)
        else:
            result = df_table_4_1_general_vehicles.loc[df_table_4_1_general_vehicles.general_vehicle_descriptions == f'{design_road_design_vehicle_type}','vehicle_length_m'].item()
            self.view.label_design_lookup_design_vehicle_length.setNum(result)
        return result

    #Calculate design_lookup_grade_adjustment_factor
    def design_lookup_grade_adjustment_factor(self):
        design_road_max_approach_grade_within_s = self.view.doubleSpinBox_design_road_max_approach_grade_within_s.value()
        design_lookup_design_vehicle_class = self.design_lookup_design_vehicle_class()
        df_table_4_6_ratio_of_acceleration_times_on_road_grades = pd.read_csv(r'resources\\railway_data\\track_and_roadway\\custom\\table_4_6_ratio_of_acceleration_times_on_road_grades.csv')

        if design_lookup_design_vehicle_class == 'No Value':
            result = 'No Value'
            self.view.label_design_lookup_grade_adjustment_factor.setText(result)
        elif design_lookup_design_vehicle_class == 'Pedestrian':
            result = 'N/A'
            self.view.label_design_lookup_grade_adjustment_factor.setText(result)
        elif design_road_max_approach_grade_within_s<-3:
            result = df_table_4_6_ratio_of_acceleration_times_on_road_grades.loc[df_table_4_6_ratio_of_acceleration_times_on_road_grades.grade_crossing_design_vehicle == f'{design_lookup_design_vehicle_class}','-4'].item()
            self.view.label_design_lookup_grade_adjustment_factor.setNum(result)
        elif design_road_max_approach_grade_within_s>=-3 and design_road_max_approach_grade_within_s<-1:
            result = df_table_4_6_ratio_of_acceleration_times_on_road_grades.loc[df_table_4_6_ratio_of_acceleration_times_on_road_grades.grade_crossing_design_vehicle == f'{design_lookup_design_vehicle_class}','-2'].item()
            self.view.label_design_lookup_grade_adjustment_factor.setNum(result)
        elif design_road_max_approach_grade_within_s>=-1 and design_road_max_approach_grade_within_s<=1:
            result = df_table_4_6_ratio_of_acceleration_times_on_road_grades.loc[df_table_4_6_ratio_of_acceleration_times_on_road_grades.grade_crossing_design_vehicle == f'{design_lookup_design_vehicle_class}','0'].item()
            self.view.label_design_lookup_grade_adjustment_factor.setNum(result)
        elif design_road_max_approach_grade_within_s>1 and design_road_max_approach_grade_within_s<=3:
            result = df_table_4_6_ratio_of_acceleration_times_on_road_grades.loc[df_table_4_6_ratio_of_acceleration_times_on_road_grades.grade_crossing_design_vehicle == f'{design_lookup_design_vehicle_class}','2'].item()
            self.view.label_design_lookup_grade_adjustment_factor.setNum(result)
        elif design_road_max_approach_grade_within_s>3:
            result = df_table_4_6_ratio_of_acceleration_times_on_road_grades.loc[df_table_4_6_ratio_of_acceleration_times_on_road_grades.grade_crossing_design_vehicle == f'{design_lookup_design_vehicle_class}','4'].item()
            self.view.label_design_lookup_grade_adjustment_factor.setNum(result)
        return result

    # ROAD GEOMETRY (GCS SECTION 6)
    #Calculate road_geometry_lookup_gradient_difference
    def road_geometry_lookup_gradient_difference(self):
        general_info_road_classification = self.view.comboBox_general_info_road_classification.currentText()
        table_6_1_difference_in_gradient = pd.read_csv(r'resources\\railway_data\\track_and_roadway\\custom\\table_6_1_difference_in_gradient.csv')

        if general_info_road_classification == '':
            result = 'No Value'
            self.view.label_road_geometry_lookup_gradient_difference.setText(result)
        else:
            result = table_6_1_difference_in_gradient.loc[table_6_1_difference_in_gradient.classification_description == f'{general_info_road_classification}','difference_in_gradient_pct'].item()
            self.view.label_road_geometry_lookup_gradient_difference.setNum(result)
        return result

    # SIGHTLINES (GCS SECTION 7)
    #Calculate sightlines_lookup_existing_active_crossing
    def sightlines_lookup_existing_active_crossing(self):
        inspection_details_gcws_type = self.view.comboBox_inspection_details_gcws_type.currentText()

        if inspection_details_gcws_type == '':
            result = 'No Value'
            self.view.label_sightlines_lookup_existing_active_crossing.setText(result)
        elif inspection_details_gcws_type == 'Active':
            result = 'Yes'
            self.view.label_sightlines_lookup_existing_active_crossing.setText(result)
        else:
            result = 'No'
            self.view.label_sightlines_lookup_existing_active_crossing.setText(result)
        return result

    #Calculate sightlines_lookup_existing_active_crossing_with_gates
    def sightlines_lookup_existing_active_crossing_with_gates(self):
        inspection_details_gcws_type = self.view.comboBox_inspection_details_gcws_type.currentText()
        gcws_observe_gates_n_or_e_approach = self.view.comboBox_gcws_observe_gates_n_or_e_approach.currentText()
        gcws_observe_gates_s_or_w_approach = self.view.comboBox_gcws_observe_gates_s_or_w_approach.currentText()

        if inspection_details_gcws_type == '' or (gcws_observe_gates_n_or_e_approach == '' and gcws_observe_gates_s_or_w_approach == ''):
            result = 'No Value'
            self.view.label_sightlines_lookup_existing_active_crossing_with_gates.setText(result)
        elif inspection_details_gcws_type == 'Active' and (gcws_observe_gates_n_or_e_approach == 'Yes' or gcws_observe_gates_s_or_w_approach == 'Yes'):
            result = 'Yes'
            self.view.label_sightlines_lookup_existing_active_crossing_with_gates.setText(result)
        else:
            result = 'No'
            self.view.label_sightlines_lookup_existing_active_crossing_with_gates.setText(result)
        return result

    #Calculate sightlines_calculate_dssd_vehicle_min_ft
    def sightlines_calculate_dssd_vehicle_min_ft(self):
        general_info_road_speed_design = self.view.spinBox_general_info_road_speed_design.value()
        design_measure_clearance_distance_vehicle = self.view.doubleSpinBox_design_measure_clearance_distance_vehicle.value()
        design_lookup_design_vehicle_class = self.design_lookup_design_vehicle_class()
        design_lookup_design_vehicle_length = self.design_lookup_design_vehicle_length()
        general_info_rail_railway_design_speed = self.general_info_rail_railway_design_speed()
        sightlines_lookup_ssd_minimum_n_or_e_approach = self.sightlines_lookup_ssd_minimum_n_or_e_approach()
        sightlines_lookup_ssd_minimum_s_or_w_approach = self.sightlines_lookup_ssd_minimum_s_or_w_approach()

        if design_lookup_design_vehicle_class == 'No Value' or general_info_rail_railway_design_speed == 'No Value' or general_info_road_speed_design == 0 or design_measure_clearance_distance_vehicle == 0.0 or sightlines_lookup_ssd_minimum_n_or_e_approach == 'No Value' or sightlines_lookup_ssd_minimum_s_or_w_approach == 'No Value' or design_lookup_design_vehicle_length == 'No Value':
            result = 'No Value'
            self.view.label_sightlines_calculate_dssd_vehicle_min_ft.setText(result)
        elif design_lookup_design_vehicle_class == 'Pedestrian':
            result = 'N/A'
            self.view.label_sightlines_calculate_dssd_vehicle_min_ft.setText(result)
        else:
            design_measure_clearance_distance_vehicle = float(design_measure_clearance_distance_vehicle)
            design_lookup_design_vehicle_length = float(design_lookup_design_vehicle_length)
            general_info_rail_railway_design_speed = int(general_info_rail_railway_design_speed)
            general_info_road_speed_design = int(general_info_road_speed_design)
            sightlines_lookup_ssd_minimum_n_or_e_approach = float(sightlines_lookup_ssd_minimum_n_or_e_approach)
            sightlines_lookup_ssd_minimum_s_or_w_approach = float(sightlines_lookup_ssd_minimum_s_or_w_approach)
            result = round(1.47 * general_info_rail_railway_design_speed * max(10,sum([max(sightlines_lookup_ssd_minimum_n_or_e_approach, sightlines_lookup_ssd_minimum_s_or_w_approach), design_measure_clearance_distance_vehicle, design_lookup_design_vehicle_length]) / (0.278* general_info_road_speed_design)), 2)
            self.view.label_sightlines_calculate_dssd_vehicle_min_ft.setNum(result)
        return result

    #Calculate sightlines_calculate_dssd_vehicle_min_m
    def sightlines_calculate_dssd_vehicle_min_m(self):
        sightlines_calculate_dssd_vehicle_min_ft = self.sightlines_calculate_dssd_vehicle_min_ft()

        if sightlines_calculate_dssd_vehicle_min_ft == 'No Value':
            result = 'No Value'
            self.view.label_sightlines_calculate_dssd_vehicle_min_m.setText(result)
        elif sightlines_calculate_dssd_vehicle_min_ft == 'N/A':
            result = 'N/A'
            self.view.label_sightlines_calculate_dssd_vehicle_min_m.setText(result)
        else:
            sightlines_calculate_dssd_vehicle_min_ft = float(sightlines_calculate_dssd_vehicle_min_ft)
            result = sightlines_calculate_dssd_vehicle_min_ft * 0.3048
            self.view.label_sightlines_calculate_dssd_vehicle_min_m.setNum(result)
        return result

    #Calculate sightlines_calculate_dstopped_pedestrian_min_ft
    def sightlines_calculate_dstopped_pedestrian_min_ft(self):
        design_calculate_clearance_time_crossing_pedestrian_design_check = self.design_calculate_clearance_time_pedestrian_design_check()
        general_info_rail_railway_design_speed = self.general_info_rail_railway_design_speed()

        if general_info_rail_railway_design_speed == 'No Value' or design_calculate_clearance_time_crossing_pedestrian_design_check == 'No Value':
            result = 'No Value'
            self.view.label_sightlines_calculate_dstopped_pedestrian_min_ft.setText(result)
        else:
            design_calculate_clearance_time_crossing_pedestrian_design_check = float(design_calculate_clearance_time_crossing_pedestrian_design_check)
            general_info_rail_railway_design_speed = int(general_info_rail_railway_design_speed)
            result = round(1.47 * general_info_rail_railway_design_speed * max(10, design_calculate_clearance_time_crossing_pedestrian_design_check),2)
            self.view.label_sightlines_calculate_dstopped_pedestrian_min_ft.setNum(result)
        return result

    #Calculate sightlines_calculate_dstopped_pedestrian_min_m
    def sightlines_calculate_dstopped_pedestrian_min_m(self):
        sightlines_calculate_dstopped_pedestrian_min_ft = self.sightlines_calculate_dstopped_pedestrian_min_ft()

        if sightlines_calculate_dstopped_pedestrian_min_ft == "No Value":
            result = "No Value"
            self.view.label_sightlines_calculate_dstopped_pedestrian_min_m.setText(result)
        else:
            sightlines_calculate_dstopped_pedestrian_min_ft = float(sightlines_calculate_dstopped_pedestrian_min_ft)
            result = round(sightlines_calculate_dstopped_pedestrian_min_ft * 0.3048, 2)
            self.view.label_sightlines_calculate_dstopped_pedestrian_min_m.setNum(result)
        return result

    #Calculate sightlines_calculate_dstopped_vehicle_min_ft
    def sightlines_calculate_dstopped_vehicle_min_ft(self):
        design_calculate_clearance_time_vehicle_design_check = self.design_calculate_clearance_time_vehicle_design_check()
        general_info_rail_railway_design_speed = self.general_info_rail_railway_design_speed()

        if design_calculate_clearance_time_vehicle_design_check == 'N/A':
            result = 'N/A'
            self.view.label_sightlines_calculate_dstopped_vehicle_min_ft.setText(result)
        elif general_info_rail_railway_design_speed == 'No Value' or design_calculate_clearance_time_vehicle_design_check == 'No Value':
            result = 'No Value'
            self.view.label_sightlines_calculate_dstopped_vehicle_min_ft.setText(result)
        else:
            design_calculate_clearance_time_crossing_vehicle_design_check = float(design_calculate_clearance_time_vehicle_design_check)
            general_info_rail_railway_design_speed = int(general_info_rail_railway_design_speed)
            result = round(1.47 * general_info_rail_railway_design_speed * max(10, design_calculate_clearance_time_crossing_vehicle_design_check),2)
            self.view.label_sightlines_calculate_dstopped_vehicle_min_ft.setNum(result)
        return result

    #Calculate sightlines_calculate_dstopped_vehicle_min_m
    def sightlines_calculate_dstopped_vehicle_min_m(self):
        sightlines_calculate_dstopped_vehicle_min_ft = self.sightlines_calculate_dstopped_vehicle_min_ft()

        if sightlines_calculate_dstopped_vehicle_min_ft == 'N/A':
            result = "N/A"
            self.view.label_sightlines_calculate_dstopped_vehicle_min_m.setText(result)
        elif sightlines_calculate_dstopped_vehicle_min_ft == "No Value":
            result = "No Value"
            self.view.label_sightlines_calculate_dstopped_vehicle_min_m.setText(result)
        else:
            sightlines_calculate_dstopped_vehicle_min_ft = float(sightlines_calculate_dstopped_vehicle_min_ft)
            result = round(sightlines_calculate_dstopped_vehicle_min_ft * 0.3048, 2)
            self.view.label_sightlines_calculate_dstopped_vehicle_min_m.setNum(result)
        return result

    #Calculate sightlines_lookup_ssd_minimum_n_or_e_approach
    def sightlines_lookup_ssd_minimum_n_or_e_approach(self):
        general_info_road_speed_design = self.view.spinBox_general_info_road_speed_design.value()
        road_geometry_road_general_approach_grade_n_or_e_approach = self.view.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.value()
        design_lookup_design_vehicle_class = self.design_lookup_design_vehicle_class()
        df_table_4_5_SSD_m_passenger_car_class = pd.read_csv(r'resources\\railway_data\\track_and_roadway\\custom\\table_4_5_SSD_m_passenger_car_class.csv')

        road_geometry_road_general_approach_grade_n_or_e_approach = round(road_geometry_road_general_approach_grade_n_or_e_approach/100.0, 0)

        if road_geometry_road_general_approach_grade_n_or_e_approach >= 0.1:
            road_geometry_road_general_approach_grade_n_or_e_approach = 0.1
        elif road_geometry_road_general_approach_grade_n_or_e_approach <= -0.1:
            road_geometry_road_general_approach_grade_n_or_e_approach = -0.1

        if general_info_road_speed_design == '' or design_lookup_design_vehicle_class == 'No Value':
            result = 'No Value'
            self.view.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setText(result)
        elif design_lookup_design_vehicle_class == 'Pedestrian':
            result = 'N/A'
            self.view.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setText(result)
        elif general_info_road_speed_design>=0.0 and general_info_road_speed_design<=10:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[0, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.view.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        elif general_info_road_speed_design>=11 and general_info_road_speed_design<=20:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[1, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.view.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        elif general_info_road_speed_design>=21 and general_info_road_speed_design<=30:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[2, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.vew.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        elif general_info_road_speed_design>=31 and general_info_road_speed_design<=40:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[3, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.view.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        elif general_info_road_speed_design>=41 and general_info_road_speed_design<=50:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[4, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.view.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        elif general_info_road_speed_design>=51 and general_info_road_speed_design<=60:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[5, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.view.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        elif general_info_road_speed_design>=61 and general_info_road_speed_design<=70:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[6, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.view.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        elif general_info_road_speed_design>=71 and general_info_road_speed_design<=80:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[7, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.view.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        elif general_info_road_speed_design>=81 and general_info_road_speed_design<=90:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[8, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.view.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        elif general_info_road_speed_design>=91 and general_info_road_speed_design<=100:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[9, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.view.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        elif general_info_road_speed_design>=101 and general_info_road_speed_design<=110:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[10, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.view.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        return result

    #Calculate sightlines_lookup_ssd_minimum_s_or_w_approach
    def sightlines_lookup_ssd_minimum_s_or_w_approach(self):
        general_info_road_speed_design = self.view.spinBox_general_info_road_speed_design.value()
        road_geometry_road_general_approach_grade_s_or_w_approach = self.view.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.value()
        design_lookup_design_vehicle_class = self.design_lookup_design_vehicle_class()
        df_table_4_5_SSD_m_passenger_car_class = pd.read_csv(r'resources\\railway_data\\track_and_roadway\\custom\\table_4_5_SSD_m_passenger_car_class.csv')

        road_geometry_road_general_approach_grade_s_or_w_approach = round(road_geometry_road_general_approach_grade_s_or_w_approach/100.0, 0)

        if road_geometry_road_general_approach_grade_s_or_w_approach >= 0.1:
            road_geometry_road_general_approach_grade_s_or_w_approach = 0.1
        elif road_geometry_road_general_approach_grade_s_or_w_approach <= -0.1:
            road_geometry_road_general_approach_grade_s_or_w_approach = -0.1
    
        if general_info_road_speed_design == '' or design_lookup_design_vehicle_class == 'No Value':
            result = 'No Value'
            self.view.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setText(result)
        elif design_lookup_design_vehicle_class == 'Pedestrian':
            result = 'N/A'
            self.view.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setText(result)
        elif general_info_road_speed_design>=0 and general_info_road_speed_design<=10:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[0, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.view.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        elif general_info_road_speed_design>=11 and general_info_road_speed_design<=20:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[1, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.view.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        elif general_info_road_speed_design>=21 and general_info_road_speed_design<=30:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[2, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.view.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        elif general_info_road_speed_design>=31 and general_info_road_speed_design<=40:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[3, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.view.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        elif general_info_road_speed_design>=41 and general_info_road_speed_design<=50:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[4, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.view.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        elif general_info_road_speed_design>=51 and general_info_road_speed_design<=60:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[5, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.view.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        elif general_info_road_speed_design>=61 and general_info_road_speed_design<=70:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[6, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.view.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        elif general_info_road_speed_design>=71 and general_info_road_speed_design<=80:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[7, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.view.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        elif general_info_road_speed_design>=81 and general_info_road_speed_design<=90:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[8, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.view.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        elif general_info_road_speed_design>=91 and general_info_road_speed_design<=100:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[9, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.view.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        elif general_info_road_speed_design>=101 and general_info_road_speed_design<=110:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[10, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.view.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        return result

        # GRADE CROSSING WARNING SYSTEM WARRANTS (GCS SECTION 9)
        #self.view.label_gcws_warrant_private_9_3.valueChanged.connect(self.gcws_warrant_private_9_3)
        #self.view.label_gcws_warrant_private_9_3_1.valueChanged.connect(self.gcws_warrant_private_9_3_1)
        #self.view.label_gcws_warrant_private_9_3_2_a.valueChanged.connect(self.gcws_warrant_private_9_3_2_a)
        #self.view.label_gcws_warrant_private_9_3_2_b.valueChanged.connect(self.gcws_warrant_private_9_3_2_b)
        #self.view.label_gcws_warrant_private_9_3_2_c.valueChanged.connect(self.gcws_warrant_private_9_3_2_c)
        #self.view.label_gcws_warrant_public_9_1.valueChanged.connect(self.gcws_warrant_public_9_1)
        #self.view.label_gcws_warrant_public_9_1_a.valueChanged.connect(self.gcws_warrant_public_9_1_a)
        #self.view.label_gcws_warrant_public_9_1_b.valueChanged.connect(self.gcws_warrant_public_9_1_b)
        #self.view.label_gcws_warrant_public_9_1_c.valueChanged.connect(self.gcws_warrant_public_9_1_c)
        #self.view.label_gcws_warrant_public_9_1_d_i.valueChanged.connect(self.gcws_warrant_public_9_1_d_i)
        #self.view.label_gcws_warrant_public_9_1_d_ii.valueChanged.connect(self.gcws_warrant_public_9_1_d_ii)
        #self.view.label_gcws_warrant_public_9_1_d_iii.valueChanged.connect(self.gcws_warrant_public_9_1_d_iii)
        #self.view.label_gcws_warrant_sidewalk_9_5.valueChanged.connect(self.gcws_warrant_sidewalk_9_5)
        #self.view.label_gates_gcws_warrant_private_9_4_1_a.valueChanged.connect(self.gates_gcws_warrant_private_9_4_1_a)
        #self.view.label_gates_gcws_warrant_private_9_4_1_b.valueChanged.connect(self.gates_gcws_warrant_private_9_4_1_b)
        #self.view.label_gates_gcws_warrant_private_9_4_1_c.valueChanged.connect(self.gates_gcws_warrant_private_9_4_1_c)
        #self.view.label_gates_gcws_warrant_public_9_2_1_a.valueChanged.connect(self.gates_gcws_warrant_public_9_2_1_a)
        #self.view.label_gates_gcws_warrant_public_9_2_1_b.valueChanged.connect(self.gates_gcws_warrant_public_9_2_1_b)
        #self.view.label_gates_gcws_warrant_public_9_2_1_c.valueChanged.connect(self.gates_gcws_warrant_public_9_2_1_c)
        #self.view.label_gates_gcws_warrant_public_9_2_1_d.valueChanged.connect(self.gates_gcws_warrant_public_9_2_1_d)
        #self.view.label_gates_gcws_warrant_public_9_2_1_e.valueChanged.connect(self.gates_gcws_warrant_public_9_2_1_e)
        #self.view.label_gates_gcws_warrant_sidewalk_9_6.valueChanged.connect(self.gates_gcws_warrant_sidewalk_9_6)

    # GRADE CROSSING WARNING SYSTEMS (GCS SECTION 12-16)
    #Calculate gcws_rail_design_warning_time_clearance_distance
    def gcws_rail_design_warning_time_clearance_distance(self):
        design_road_design_vehicle_type = self.view.comboBox_design_road_design_vehicle_type.currentText()
        design_measure_clearance_distance_pedestrian = self.view.doubleSpinBox_design_measure_clearance_distance_pedestrian.value()
        design_measure_clearance_distance_vehicle = self.view.doubleSpinBox_design_measure_clearance_distance_vehicle.value()

        if design_road_design_vehicle_type == '' or (design_measure_clearance_distance_pedestrian == 0.0 and design_measure_clearance_distance_vehicle == 0.0):
            result = 'No Value'
            self.view.label_gcws_rail_design_warning_time_clearance_distance.setText(result)
        elif design_road_design_vehicle_type == 'Pedestrian Only' and design_measure_clearance_distance_pedestrian != 0.0:
            result = math.ceil(max(20, sum([20, math.ceil(design_measure_clearance_distance_pedestrian - 11.0) / 3.0])))
            self.view.label_gcws_rail_design_warning_time_clearance_distance.setNum(result)
        else:
            result = math.ceil(max(20, sum([20, math.ceil(design_measure_clearance_distance_vehicle - 11.0) / 3.0])))
            self.view.label_gcws_rail_design_warning_time_clearance_distance.setNum(result)
        return result
    
    #Calculate gcws_rail_design_warning_time_departure_time_vehicle
    def gcws_rail_design_warning_time_departure_time_vehicle(self):
        design_calculate_clearance_time_vehicle_design_check = self.design_calculate_clearance_time_vehicle_design_check()

        if design_calculate_clearance_time_vehicle_design_check == 'N/A':
            result = 'N/A'
            self.view.label_gcws_rail_design_warning_time_departure_time_vehicle.setText(result)
        elif design_calculate_clearance_time_vehicle_design_check == 'No Value':
            result = 'No Value'
            self.view.label_gcws_rail_design_warning_time_departure_time_vehicle.setText(result)
        else:
            design_calculate_clearance_time_crossing_vehicle_design_check = float(design_calculate_clearance_time_vehicle_design_check)
            result = math.ceil(design_calculate_clearance_time_crossing_vehicle_design_check)
            self.view.label_gcws_rail_design_warning_time_departure_time_vehicle.setNum(result)
        return result

    #Calculate gcws_rail_design_warning_time_departure_time_pedestrian
    def gcws_rail_design_warning_time_departure_time_pedestrian(self):
        design_calculate_clearance_time_crossing_pedestrian_design_check = self.design_calculate_clearance_time_pedestrian_design_check()

        if design_calculate_clearance_time_crossing_pedestrian_design_check == 'No Value':
            result = 'No Value'
            self.view.label_gcws_rail_design_warning_time_departure_time_pedestrian.setText(result)
        else:
            design_calculate_clearance_time_crossing_pedestrian_design_check = float(design_calculate_clearance_time_crossing_pedestrian_design_check)
            result = math.ceil(design_calculate_clearance_time_crossing_pedestrian_design_check)
            self.view.label_gcws_rail_design_warning_time_departure_time_pedestrian.setNum(result)
        return result

    #TODO
    #Calculate gcws_rail_design_warning_time_gate_arm_clearance
    def gcws_rail_design_warning_time_gate_arm_clearance(self):
        design_calculate_gate_arm_clearance_time_vehicle_recommended = self.design_calculate_gate_arm_clearance_time_vehicle_recommended()
        gates_gcws_rail_gate_arm_descent_time_design = self.view.doubleSpinBox_gates_gcws_rail_gate_arm_descent_time_design.value()

        if design_calculate_gate_arm_clearance_time_vehicle_recommended == 'No Value' or gates_gcws_rail_gate_arm_descent_time_design == 0.0:
            result = 'No Value'
            self.view.label_gcws_rail_design_warning_time_gate_arm_clearance.setText(result)
        else:
            result = math.ceil(sum([design_calculate_gate_arm_clearance_time_vehicle_recommended, gates_gcws_rail_gate_arm_descent_time_design, 5.0]))
            self.view.label_gcws_rail_design_warning_time_gate_arm_clearance.setNum(result)
        return result

    #TODO
    #Calculate gcws_rail_design_warning_time_ssd
    def gcws_rail_design_warning_time_ssd(self):
        sightlines_lookup_ssd_minimum_n_or_e_approach = self.sightlines_lookup_ssd_minimum_n_or_e_approach()
        sightlines_lookup_ssd_minimum_s_or_w_approach = self.sightlines_lookup_ssd_minimum_s_or_w_approach()
        design_road_design_vehicle_type = self.view.comboBox_design_road_design_vehicle_type.currentText()
        design_calculate_vehicle_travel_distance = self.design_calculate_vehicle_travel_distance()
        general_info_road_speed_design = self.view.spinBox_general_info_road_speed_design.value()

        if sightlines_lookup_ssd_minimum_n_or_e_approach == 'No Value' or sightlines_lookup_ssd_minimum_s_or_w_approach == 'No Value' or design_road_design_vehicle_type == '' or design_calculate_vehicle_travel_distance == 'No Value' or general_info_road_speed_design == 0:
            result = 'No Value'
            self.view.label_gcws_rail_design_warning_time_ssd.setText(result)
        elif design_road_design_vehicle_type == 'Pedestrian Only':
            result = 'N/A'
            self.view.label_gcws_rail_design_warning_time_ssd.setText(result)
        else:
            result = math.ceil(sum([max(sightlines_lookup_ssd_minimum_n_or_e_approach, sightlines_lookup_ssd_minimum_s_or_w_approach), design_calculate_vehicle_travel_distance]) * 3600 / (general_info_road_speed_design * math.pow(10, 3)))
            self.view.label_gcws_rail_design_warning_time_ssd.setNum(result)
        return result
    
    #TODO
    #Calculate gcws_rail_design_warning_time_adjacent_crossing
    def gcws_rail_design_warning_time_adjacent_crossing(self):
        pass
    
    #TODO
    #Calculate gcws_rail_design_approach_warning_time
    def gcws_rail_design_approach_warning_time(self):
        pass
        gcws_rail_design_warning_time_preemption = self.view.spinBox_gcws_rail_design_warning_time_preemption.value()
        gcws_rail_design_warning_time_clearance_distance = self.gcws_rail_design_warning_time_clearance_distance()
        gcws_rail_design_warning_time_departure_time_vehicle = self.gcws_rail_design_warning_time_departure_time_vehicle()
        gcws_rail_design_warning_time_departure_time_pedestrian = self.gcws_rail_design_warning_time_departure_time_pedestrian()
        gcws_rail_design_warning_time_gate_arm_clearance = self.gcws_rail_design_warning_time_gate_arm_clearance() 
        gcws_rail_design_warning_time_ssd = self.gcws_rail_design_warning_time_ssd()

        gcws_rail_design_approach_warning_time = {
            'gcws_rail_design_warning_time_preemption': gcws_rail_design_warning_time_preemption,
            'gcws_rail_design_warning_time_clearance_distance': gcws_rail_design_warning_time_clearance_distance, 
            'gcws_rail_design_warning_time_departure_time_vehicle': gcws_rail_design_warning_time_departure_time_vehicle, 
            'gcws_rail_design_warning_time_departure_time_pedestrian': gcws_rail_design_warning_time_departure_time_pedestrian,
            'gcws_rail_design_warning_time_gate_arm_clearance': gcws_rail_design_warning_time_gate_arm_clearance, 
            'gcws_rail_design_warning_time_ssd': gcws_rail_design_warning_time_ssd
        }
         
        #for i in gcws_rail_design_approach_warning_time:
        #    print (i)

        #return gcws_rail_design_approach_warning_time

    # GATES FOR GRADE CROSSING WARNING SYSTEMS (GCS SECTION 10, 12, 15)
    #TODO
    #Calculate gates_gcws_calculate_inner_gate_arm_delay_time_recommended
    def gates_gcws_calculate_inner_gate_arm_delay_time_recommended(self):
        design_calculate_adjacent_track_clearance_time = self.design_calculate_adjacent_track_clearance_time()

        if design_calculate_adjacent_track_clearance_time == 'No Value':
            result = design_calculate_adjacent_track_clearance_time
            self.view.label_gcws_rail_design_warning_time_ssd.setText(result)
        else:
            result = design_calculate_adjacent_track_clearance_time
            self.view.label_gcws_rail_design_warning_time_ssd.setNum(result)  
        return result

    # PREPARE TO STOP AT RAILWAY CROSSING SIGN (GCS SECTION 18)
    #TODO
    #Calculate aawd_calculate_advance_activation_time_design_n_or_e_approach
    def aawd_calculate_advance_activation_time_design_n_or_e_approach(self):
        general_info_road_speed_design = self.view.spinBox_general_info_road_speed_design.value()
        design_calculate_vehicle_travel_distance = self.design_calculate_vehicle_travel_distance()
        aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended = self.aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended()

        if general_info_road_speed_design == 0 or design_calculate_vehicle_travel_distance == "No Value" or aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended == "No Value":
            result = "No Value"
            self.view.label_aawd_calculate_advance_activation_time_design_n_or_e_approach.setText(result)
        else:
            result = round(3.6 * sum([design_calculate_vehicle_travel_distance, aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended]) / general_info_road_speed_design, 2)
            self.view.label_aawd_calculate_advance_activation_time_design_n_or_e_approach.setNum(result)
        return result

    #TODO
    #Calculate aawd_calculate_advance_activation_time_design_s_or_w_approach    
    def aawd_calculate_advance_activation_time_design_s_or_w_approach(self):
        general_info_road_speed_design = self.view.spinBox_general_info_road_speed_design.value()
        design_calculate_vehicle_travel_distance = self.design_calculate_vehicle_travel_distance()
        aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended = self.aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended()

        if general_info_road_speed_design == 0 or design_calculate_vehicle_travel_distance == 'No Value' or aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended == 'No Value':
            result = 'No Value'
            self.view.label_aawd_calculate_advance_activation_time_design_n_or_e_approach.setText(result)
        else:
            result = round(3.6 * sum([design_calculate_vehicle_travel_distance, aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended]) / general_info_road_speed_design, 2)
            self.view.label_aawd_calculate_advance_activation_time_design_n_or_e_approach.setNum(result)
        return result

    #TODO
    #Calculate aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended
    def aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended(self):
        general_info_road_speed_posted = self.view.spinBox_general_info_road_speed_posted.value()
        road_geometry_road_general_approach_grade_n_or_e_approach = self.view.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.value()
        road_geometry_road_general_approach_grade_s_or_w_approach = self.view.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.value()
        design_input_reaction_time = self.view.label_design_input_reaction_time.text()
        deceleration_rate = 2.6 #typically 2.6m/s2
        gravitational_acceleration = 9.81 #typically 9.81m/s2)

        if general_info_road_speed_posted == 0 or road_geometry_road_general_approach_grade_n_or_e_approach == 0.0 or road_geometry_road_general_approach_grade_s_or_w_approach == 0.0:
            result = 'No Value'
            self.view.label_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended.setText(result)
        else:
            result = sum([general_info_road_speed_posted * design_input_reaction_time / 3.6, math.pow(general_info_road_speed_posted, 2) / (25.92 * sum([deceleration_rate, road_geometry_road_general_approach_grade_n_or_e_approach * gravitational_acceleration])) ])
            self.view.label_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended.setNum(result)
        return result

    #TODO
    #Calculate aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended
    def aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended(self):
        general_info_road_speed_posted = self.view.spinBox_general_info_road_speed_posted.value()
        road_geometry_road_general_approach_grade_n_or_e_approach = self.view.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.value()
        road_geometry_road_general_approach_grade_s_or_w_approach = self.view.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.value()
        design_input_reaction_time = self.view.label_design_input_reaction_time.text()
        deceleration_rate = 2.6 #typically 2.6m/s2
        gravitational_acceleration = 9.81 #typically 9.81m/s2)

        if general_info_road_speed_posted == 0 or road_geometry_road_general_approach_grade_n_or_e_approach == 0.0 or road_geometry_road_general_approach_grade_s_or_w_approach == 0.0:
            result = 'No Value'
            self.view.label_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended.setText(result)
        else:
            result = sum([general_info_road_speed_posted * design_input_reaction_time / 3.6, math.pow(general_info_road_speed_posted, 2) / (25.92 * sum([deceleration_rate, road_geometry_road_general_approach_grade_s_or_w_approach * gravitational_acceleration])) ])
            self.view.label_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended.setNum(result)
        return result

    #TODO
    #Calculate aawd_warrant_gcr_lookup_road_classification
    def aawd_warrant_gcr_lookup_road_classification(self):
        general_info_road_classification = self.view.comboBox_general_info_road_classification.currentText()
        general_info_road_classification.split()

        if general_info_road_classification == '':
            result = 'No Value'
            self.view.label_aawd_warrant_gcr_lookup_road_classification.setText(result)
        elif general_info_road_classification[1] == 'Freeway':
            result = 'Yes'
            self.view.label_aawd_warrant_gcr_lookup_road_classification.setText(result)
        else:
            result = 'No'
            self.view.label_aawd_warrant_gcr_lookup_road_classification.setText(result)
        return result

    #Calculate aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr
    def aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr(self):
        general_info_road_speed_design = self.view.spinBox_general_info_road_speed_design.value()

        if general_info_road_speed_design == '':
            result = 'No Value'
            self.view.label_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr.setText(result)
        elif general_info_road_speed_design > 90:
            result = 'Yes'
            self.view.label_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr.setText(result)
        else:
            result = 'No'
            self.view.label_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr.setText(result)
        return result
        #self.spinBox_general_info_road_speed_design
    
    # INTERCONNECTION OF TRAFFIC SIGNALS (GCS SECTION 19)
    #Calculate preemption_of_traffic_signals_lookup_proximity_condition
    def preemption_of_traffic_signals_lookup_proximity_condition(self):
        location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach = self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach.value()
        location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach = self.view.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach.value()

        if location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach == 0.00 and location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach == 0.00:
            result = 'No Value'
            self.view.label_preemption_of_traffic_signals_lookup_proximity_condition.setText(result)
        elif (location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach > 0.00 and location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach <30.00) or (location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach > 0.00 and location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach < 30.00):
            result = 'Yes'
            self.view.label_preemption_of_traffic_signals_lookup_proximity_condition.setText(result)
        else:
            result = 'No'
            self.view.label_preemption_of_traffic_signals_lookup_proximity_condition.setText(result)
        return result

    #Calculate preemption_of_traffic_signals_lookup_required
    def preemption_of_traffic_signals_lookup_required(self):
        general_info_rail_railway_design_speed = self.general_info_rail_railway_design_speed()
        preemption_of_traffic_signals_lookup_proximity_condition = self.preemption_of_traffic_signals_lookup_proximity_condition()

        if general_info_rail_railway_design_speed == 0 or preemption_of_traffic_signals_lookup_proximity_condition == 'No Value':
            result = 'No Value'
            self.view.label_preemption_of_traffic_signals_lookup_required.setText(result)
        elif general_info_rail_railway_design_speed > 15 and preemption_of_traffic_signals_lookup_proximity_condition == 'Yes':
            result = 'Yes'
            self.view.label_preemption_of_traffic_signals_lookup_required.setText(result)
        else: 
            result = 'No'
            self.view.label_preemption_of_traffic_signals_lookup_required.setText(result)
        return result

    # WHISTLE CESSATION (GCS SECTION Appendix D)
    #Group Labels
    #TODO
    #Calculate areas_without_train_whistling_lookup_gcs_9_2
    def areas_without_train_whistling_lookup_gcs_9_2(self):
        pass
        #self.view.comboBox_gcws_observe_gates_n_or_e_approach
        #self.view.comboBox_gcws_observe_gates_s_or_w_approach
        #self.view.label_gates_gcws_warrant_public_9_2_1_a
        #self.view.label_gates_gcws_warrant_public_9_2_1_b
        #self.view.label_gates_gcws_warrant_public_9_2_1_c
        #self.view.label_gates_gcws_warrant_public_9_2_1_d
        #self.view.label_gates_gcws_warrant_public_9_2_1_e

    #Calculate areas_without_train_whistling_requirements_lookup_table_d1_criteria
    def areas_without_train_whistling_requirements_lookup_table_d1_criteria(self):
        general_info_rail_no_tracks_total = self.general_info_rail_no_tracks_total()
        general_info_rail_railway_design_speed = self.general_info_rail_railway_design_speed()

        if general_info_rail_no_tracks_total == 'No Value' or general_info_rail_railway_design_speed == 'No Value':
            result = 'No Value'
            self.view.label_areas_without_train_whistling_requirements_lookup_table_d1_criteria.setText(result)
        elif (general_info_rail_no_tracks_total == 1 and general_info_rail_railway_design_speed > 0 and general_info_rail_railway_design_speed <= 50) or (general_info_rail_no_tracks_total >= 2 and general_info_rail_railway_design_speed > 0 and general_info_rail_railway_design_speed <= 15):
            result = 'FLB'
            self.view.label_areas_without_train_whistling_requirements_lookup_table_d1_criteria.setText(result)
        elif (general_info_rail_no_tracks_total == 1 and general_info_rail_railway_design_speed > 50) or (general_info_rail_no_tracks_total >= 2 and general_info_rail_railway_design_speed > 15):
            result = 'FLBG'
            self.view.label_areas_without_train_whistling_requirements_lookup_table_d1_criteria.setText(result) 
        else:
            result = 'NULL RESULT'
            self.view.label_areas_without_train_whistling_requirements_lookup_table_d1_criteria.setText(result)
        return result

    #TODO
    #Calculate areas_without_train_whistling_requirements_observe_table_D1
    def areas_without_train_whistling_requirements_observe_table_D1(self):
        gcws_observe_gates_n_or_e_approach = self.view.comboBox_gcws_observe_gates_n_or_e_approach.currentText()
        gcws_observe_gates_s_or_w_approach = self.view.comboBox_gcws_observe_gates_s_or_w_approach.currentText()
        gcws_observe_light_units_n_or_e_approach = self.view.comboBox_gcws_observe_light_units_n_or_e_approach.currentText()
        gcws_observe_light_units_s_or_w_approach = self.view.comboBox_gcws_observe_light_units_s_or_w_approach.currentText()
        areas_without_train_whistling_requirements_lookup_table_d1_criteria = self.areas_without_train_whistling_requirements_lookup_table_d1_criteria()

        print(gcws_observe_gates_n_or_e_approach)
        print(gcws_observe_gates_s_or_w_approach)
        print(gcws_observe_light_units_n_or_e_approach)
        print(gcws_observe_light_units_s_or_w_approach)
        print(areas_without_train_whistling_requirements_lookup_table_d1_criteria)


        if gcws_observe_gates_n_or_e_approach == '' or gcws_observe_gates_s_or_w_approach == '' or gcws_observe_light_units_n_or_e_approach == '' or gcws_observe_light_units_s_or_w_approach == '' or areas_without_train_whistling_requirements_lookup_table_d1_criteria == 'No Value':
            result = 'No Value'
            self.view.label_areas_without_train_whistling_requirements_observe_table_D1.setText(result)
            print('condition1')
        elif ((gcws_observe_gates_n_or_e_approach == 'Yes' and gcws_observe_gates_s_or_w_approach == 'Yes') and areas_without_train_whistling_requirements_lookup_table_d1_criteria == 'FLBG'):
            result = 'Yes'
            self.view.label_areas_without_train_whistling_requirements_observe_table_D1.setText(result)
        elif ((gcws_observe_gates_n_or_e_approach == 'No' or gcws_observe_gates_s_or_w_approach == 'No') and areas_without_train_whistling_requirements_lookup_table_d1_criteria == 'FLBG'):
            result = 'No'
            self.view.label_areas_without_train_whistling_requirements_observe_table_D1.setText(result)
            print('condition2')
        elif (gcws_observe_light_units_n_or_e_approach == 'Yes' and gcws_observe_light_units_s_or_w_approach == 'Yes' and areas_without_train_whistling_requirements_lookup_table_d1_criteria == 'FLB'):
            result = 'Yes'
            self.view.label_areas_without_train_whistling_requirements_observe_table_D1.setText(result)
            print('condition3')
        else:
            result = 'No'
            self.view.label_areas_without_train_whistling_requirements_observe_table_D1.setText(result)
            print('condition4')
        print(result)
        return result

