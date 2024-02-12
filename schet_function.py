import asyncio
import osmnx as ox
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
from aiogram import Router, F, Bot
from aiogram.types import Message


async def path_long(start_loc, finish_loc):
    print(start_loc)
    print(finish_loc)
    geolocator = Nominatim(user_agent="tvasilev577@gmail.com")
    location = geolocator.reverse(f'{start_loc[1]}, {start_loc[0]}', language="en")
    b = location.address.split(',')[3:]
    print(','.join(b))
    locat_for_find = ','.join(b).strip()

    #G = ox.graph_from_place('New York, USA', network_type='drive')
    G = ox.graph_from_place(locat_for_find, network_type='drive')

    latitude = start_loc[1]
    longitude = start_loc[0]

    # Координаты ESB
    latitude_ESB = finish_loc[1]
    longtitude_ESB = finish_loc[0]

    ESB_point = latitude_ESB, longtitude_ESB

    ude = latitude, longitude

    nearest_edge_ESB = ox.distance.nearest_edges(G, ESB_point, ude)
    print(nearest_edge_ESB[0][0])
    print(nearest_edge_ESB[1][0])
    route = nx.shortest_path(G, nearest_edge_ESB[0][0], nearest_edge_ESB[1][0])

    G = ox.add_edge_speeds(G)
    G = ox.add_edge_travel_times(G)
    route_length = int(sum(ox.utils_graph.get_route_edge_attributes(G, route, 'length')))
    route_time = int(sum(ox.utils_graph.get_route_edge_attributes(G, route, 'travel_time')))
    print('Route  is', route_length / 1000 , 'kilometrs and takes', route_time / 60, 'minutes.')


async def send_loading_message(message: Message, bot: Bot, location, adress):
    # Send initial loading message
    loading_message = await message.answer("Загрузка: ⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ - 0%")

    # Run long function in background
    task = asyncio.create_task(path_long(location, adress))  # Replace ... with your function arguments

    # Update loading message with progress
    for percent in range(0, 101, 10):
        await asyncio.sleep(1)  # Simulate delay
        loading_progress = '🟩' * (percent // 10) + '⬜️' * ((100 - percent) // 10)
        await bot.edit_message_text(
            loading_progress,
            chat_id=message.from_user.id,
            message_id=message.message_id
        )
    
    # Wait for task completion
    await task

    # Update loading message when task is completed
    await bot.edit_message_text(
        "Расчёт завершён! Спасибо за ожидание.",
        chat_id=message.from_user.id,
        message_id=message.message_id
    )