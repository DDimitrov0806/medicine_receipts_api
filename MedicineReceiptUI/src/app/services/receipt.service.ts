import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { lastValueFrom } from 'rxjs';
import { Receipt } from '../models/receipt.model';

const baseUrl = 'http://localhost:8080/api/receipts';

@Injectable({
  providedIn: 'root'
})
export class ReceiptService {

  constructor(private http: HttpClient) { }

  async getAll(): Promise<Receipt[]> {
    return await lastValueFrom(this.http.get<Receipt[]>(`${baseUrl}`));
  }

  async get(id: number): Promise<Receipt> {
    return await lastValueFrom(this.http.get<Receipt>(`${baseUrl}/${id}`));
  }

  async create(data: Receipt) {
    return await lastValueFrom(this.http.post(baseUrl, data));
  }

  async update(id: number, data: Receipt) {
    return await lastValueFrom(this.http.put(`${baseUrl}/${id}`, data));
  }

  async delete(id: number) {
    return await lastValueFrom(this.http.delete(`${baseUrl}/${id}`));
  }
}
